
# this will multiply all the even numbers by themselves
def multiply_evens(num_list):
    return [num * num for num in num_list if num % 2 == 0]

answer = multiply_evens([2,3,4,5,6])
print(answer)

# this will multiply all the even numbers and return their product
def multiply_even_numbers(_list):
    total = 1
    for val in _list:
        if val % 2 == 0:
            total *= val
    return total


answer = multiply_even_numbers([2,3,4,5,6])
print(answer)

# this will multiply all the even numbers and return their product
import functools, operator

def multiply_all_evens(list_num):
    return functools.reduce(operator.mul, [val for val in list_num if val % 2 == 0], 1)

print(multiply_all_evens([2,3,4,5,6]))
