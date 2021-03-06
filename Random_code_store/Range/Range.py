##Range
#The range function creates a sequential list of numbers. usually starts from the least to the max
numbers=list(range(10))
print(numbers)
#The call to list is necessary because range by itself will create a range object. 
# This will be needed to be converted to a list for it to be used later.

nums=list(range(5))
print(nums[4])

# this is alot different because the normal way of counting is len(nums) with a total of 5 items (0,1,2,3,4,5)
nums[0]=0
nums[1]=1
nums[2]=2
nums[3]=3
nums[4]=4

#If a range is called with one argument. It produces an object with values from 0 to that argument. in other words an argument 10 will have an output of 0 to 10
#If a range is called with two arguments. It produces values from the first to the second.

numbers=list(range(3,8))
print(numbers)

print(range)==range(0,20)

num=20
print(range(num))
print(list(range(num)))


#the range always starts with the first argument and stops at a value below the last argument
nums=list(range(5,8))
print(len(nums))


#A range can have a third argument, this determines the interval of the sequence produced.
#the third argument must always be an integer.

numbers=list(range(5,20,2))
print(numbers)


nums= list(range(3,15,3))
print(nums[2])



