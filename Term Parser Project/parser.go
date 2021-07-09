package term

import (
	"errors"
	"strconv"
)

// ErrParser is the error value returned by the Parser if the string is not a
// valid term.
// See also https://golang.org/pkg/errors/#New
// and // https://golang.org/pkg/builtin/#error
var ErrParser = errors.New("parser error")

//
// <term>     ::= ATOM | NUM | VAR | <compound>
// <compound> ::= <functor> LPAR <args> RPAR
// <functor>  ::= ATOM
// <args>     ::= <term> | <term> COMMA <args>
//

// Parser is the interface for the term parser.
// Do not change the definition of this interface.
type Parser interface {
	Parse(string) (*Term, error)
}

// NewParser creates a struct of a type that satisfies the Parser interface.
func NewParser() Parser {
	return &ParserImpl{
		lex:         nil,
		peekTok:     nil,
		terms:       make(map[string]*Term),
		termID:      make(map[*Term]int),
		termCounter: 0,
	}
}

// Code taken from professor Thakur's hw solutions videos
type ParserImpl struct {
	// lexer, initialized at eac h call to Parse
	lex *lexer
	// lookahead token, initialized at eachb call to Parse
	peekTok *Token
	// Map from string representing a term to an actual term
	terms map[string]*Term
	// map from term to its ID
	termID map[*Term]int
	// Counter
	termCounter int
}

func (p *ParserImpl) nextToken() (*Token, error) {
	if tok := p.peekTok; tok != nil {
		p.peekTok = nil
		return tok, nil
	}
	return p.lex.next()
}

func (p *ParserImpl) backToken(tok *Token) {
	p.peekTok = tok
}

func (p *ParserImpl) Parse(input string) (*Term, error) {
	p.lex = newLexer(input)
	p.peekTok = nil

	// if input is empty
	tok, err := p.nextToken()
	if err != nil {
		return nil, ErrParser
	}
	if tok.typ == tokenEOF {
		return nil, nil
	}
	p.backToken(tok)
	term, err := p.parseNextTerm() //
	// term, err := p.termNT // table driven parser
	if err != nil {
		return nil, ErrParser
	}
	// error if we have not consumed all of the input
	if tok, err := p.nextToken(); err != nil || tok.typ != tokenEOF {
		return nil, ErrParser
	}
	return term, nil
}

// parseNextTerm parses a prefix of the string, via lexer, into a term or returns an error
func (p *ParserImpl) parseNextTerm() (*Term, error) {
	tok, err := p.nextToken()
	if err != nil {
		return nil, err
	}
	switch tok.typ {
	case tokenEOF:
		return nil, nil
	case tokenNumber:
		return p.makeSimpleTerm(TermNumber, tok.literal), nil
	case tokenVariable:
		return p.makeSimpleTerm(TermVariable, tok.literal), nil
	case tokenAtom:
		a := p.makeSimpleTerm(TermAtom, tok.literal)
		nxt, err := p.nextToken()
		if err != nil {
			return nil, err
		}
		if nxt.typ != tokenLpar {
			// Atom is not the functor for a compound term
			p.backToken(nxt)
			return a, nil
		}
		// Atom might be the functor of a compund term
		arg, err := p.parseNextTerm()
		if err != nil {
			return nil, err
		}
		// args of a compound term contains at least one term
		args := []*Term{arg}
		nxt, err = p.nextToken()
		if err != nil {
			return nil, err
		}
		// Parse the rest of the arguments, if any.
		for ; nxt.typ == tokenComma; nxt, err = p.nextToken() {
			arg, err = p.parseNextTerm()
			if err != nil {
				return nil, err
			}
			args = append(args, arg)
		}
		if nxt.typ != tokenRpar {
			return nil, ErrParser
		}
		return p.makeCompoundTerm(a, args), nil
	default:
		return nil, ErrParser
	}

}

// helper functions for making terms

// makesimpleterm makes a simple term
func (p *ParserImpl) makeSimpleTerm(typ TermType, lit string) *Term {
	key := lit
	term, ok := p.terms[key]
	if !ok {
		term = &Term{Typ: typ, Literal: lit}
		p.insertTerm(term, key)
	}
	return term
}

// makecompoundterm makes a compound term
func (p *ParserImpl) makeCompoundTerm(functor *Term, args []*Term) *Term {
	key := strconv.Itoa(p.termID[functor])
	for _, arg := range args {
		key += ", " + strconv.Itoa(p.termID[arg])
	}
	term, ok := p.terms[key]
	if !ok {
		term = &Term{
			Typ:     TermCompound,
			Functor: functor,
			Args:    args,
		}
		p.insertTerm(term, key)
	}
	return term
}

// inserts term with given key into the terms and termID maps
func (p *ParserImpl) insertTerm(term *Term, key string) {
	p.terms[key] = term
	p.termID[term] = p.termCounter
	p.termCounter++
}
