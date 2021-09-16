#  Program created by Brayan Vera. Date 08/30/21

#  Program name: Valid_Parenthesis
#  This program returns True when valid parenthesis are entered.
#  The program returns False otherwise.
#  Open brackets must be closed in the correct order.
#  Open brackets must be closed by the same type of brackets.
#  Example:
#  Input: s = "()"     , Output: true
#  Input: s = "()[]{}" , Output: true
#  Input: s = "(]"     , Output: false
#  Input: s = "([)]"   , Output: false
#  Input: s = "{[]}"   , Output: true
def valid_parenthesis(s):

    left_par_check = 0
    left_curl_check = 0
    left_bra_check = 0
    right_par_check = 0
    right_curl_check = 0
    right_bra_check = 0
    count_s = 0
    # Checks if the given string of parenthesis are uneven, which means that one parenthesis is missing.
    if len(s) % 2 == 1:
        print("False, uneven parenthesis.")
        return False
    if s[0] in [")", "}", "]"]:
        print("False for invalid at beginning.")
        return False
    if s[len(s) - 1] in ["(", "{", "["]:
        print("False for the last invalid.")
        return False
    # Even parenthesis. checks that each par has its pair.
    for par in s:
        count_s += 1
        if par == "(":
            found_par = 0
            left_par_check += 1
            #  This loop skips one value starting at index 1.
            for next_par in s[count_s::2]:
                if next_par == ")":
                    found_par += 1
                    #print("the ) was found")
                    continue
                # If invalid next to left open parenthesis.
                if s[count_s] in ["}","]"]:
                    #print("----returning false for next to invalid-----")
                    return False
            #  When no found pair, return False.
            if found_par == 0:
                #print("There was no ) found returning False")
                print("Not valid: FALSE")
                return False

        elif par == "{":
            found_par = 0
            left_curl_check += 1 
            for next_par in s[count_s::2]:
                if next_par == "}":
                    found_par += 1
                    #print("the } was found")
                    continue
                if s[count_s] in [")", "]"]:
                    #print("----returning false for next to invalid-----")
                    return False
            if found_par == 0:
                #print("There was no } found returning False")
                print("Not valid: FALSE")
                return False

        elif par == "[":
            found_par = 0
            left_bra_check += 1 #3
            for next_par in s[count_s::2]:
                if next_par == "]":
                    found_par += 1
                    #print("the ] was found")
                    continue
                if s[count_s] in [")", "}"]:
                    #print("----returning false for next to invalid-----")
                    return False
            if found_par == 0:
                #print("There was no ] found returning false")
                print("Not valid: FALSE")
                return False

        elif par == ")":
            right_par_check += 1
        elif par == "}":
            right_curl_check += 1
        elif par == "]":
            right_bra_check += 1
        #  returning true, meaning everything went fine.
        if count_s == len(s):
            if left_par_check == right_par_check and left_curl_check == right_curl_check and left_bra_check == right_bra_check:
                print("Valid parenthesis: TRUE")
                return True
            else:
                print("Uneven parenthesis: FALSE")
                return False

    print("Output is False")
    return False

def main():
    parenthesis = "{[]}"           #User input HERE
    valid_parenthesis(parenthesis)

if __name__ == "__main__":
    main()