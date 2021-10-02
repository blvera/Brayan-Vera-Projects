# Program created by Brayan Vera. Date 09/16/21

# Creating a class
class MyRange:
    #Making a start point and an end point
    #self is the instance, the object
    
    def __init__(self,start,end):
        self.value = start
        self.end = end

    #now we want to make this class iterable.
    #passing self to know the state where the itertion is at.
    def __iter__(self):
        return self #<-- now this object needs add a  __next__ method to this class.
    
    def __next__(self):
        #Checking if the iterable has values.
        if self.value <= self.end:
            raise StopIteration
        current = self.value
        self.value += 1 #I want to increment this so we can know that we are actually iterating through something
        return current

# Now let's try it to see if it works.
nums = MyRange(1,10)

# Now, let's loop through this.
# for val in nums:
#     print(val)

# print(next(nums))