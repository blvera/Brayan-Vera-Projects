# Program created by Brayan Vera
# Program Date: Oct 7, 2021

'''
Write a function 'fib(n)' that takes in a number as an argument.
The function should return the n-th number of the Fibonacci sequence.

The 1st and 2nd number of the sequence is 1.
To generate the next number of the sequence, we sum the previous two.

example:
fib(n): 1,1,2,3,5,8,13,21,34, ...


Time complexity: O(2^n) time
Space Complexity: O(n) space
'''
# Coded in memoized complexity!!!!
def fib(n,memo):

    if n in memo:
        return memo[n]
    if n < 3:
        return 1
    memo[n] = fib(n-1, memo)+fib(n-2,memo)

    return memo[n]
'''
Making the Time complexity much better, to spend less time.
-Capturing duplicate sub problems
-Store the results I get (so we can use the stored data if we want to reclaculate the sub problems)
*Implementing "Memoization" which is a strategy to solve any dynamic programming problem now.
 (Memoization works as a reminder to myself) - using "HASH MAP" equivalent.
'''

def main():
    n = 50
    memo = {}
    print(fib(n,memo))

if __name__ == "__main__":
    main()

#WORKS NOW, BUT CANNOT HANDLE TO RETURN LARGE NUMBERS SUCH AROUND ABOVE the 35th index place.