# first, create a list to itearate over
# then define a function that will double the numbers in  list
# create a variable that will map over the list and use the function and use list()

nums = [2,4,6,8,10]
def double(x):
    return x * 2

doubles = list(map(double, nums))
print(doubles)


# using a lambda function, map, list 
# first we pass the lambda with one parameter, then the calculation, and then the list 
nums1 = [1,3,5,7,9]
triples = list(map(lambda x: x * 3, nums1))
print(triples)
