def sum_values(*args):
    total = 0
    for num in args:
        total += num
    return total

nums = [1,2,3,4,5,6]
print(sum_values(*nums))



def add_mult(a,b,c, **kwargs):
    print(a+b*c)
    print(kwargs)

data = dict(a=2, b=3, c=4, name="tony stark", age=55)
print(add_mult(**data, cat="blue"))