

'''
Problem Topic: Grid Traveler Memoization
- Say that you are a traveler on a 2D grid. You begin in the top-left corner 
and your goal is to travel to the bottom-right corner. You may only move down or right.

-In how many ways can you travel to the goal on a grid with dimensions m*n?

-Write a function 'gridTraveler(m,n)' that calculates this.
'''



 

def main():
    n = 50
    memo = {}
    print(fib(n,memo))

if __name__ == "__main__":
    main()


'''
Examples:
gridTravel(2,3) - > 3
    1. right, right, down
    2. right, down, right
    3. down, right, right
gridTravel(1,1) - > 1
    1. "do nothing"
gridTravel(0,1) - > 0
gridTravel(1,0) - > 0
gridTravel(0,0) - > 0
'''