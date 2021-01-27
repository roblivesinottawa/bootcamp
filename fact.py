# def fact(n):
#     if n < 2:
#         return 1
#     return n * fact(n - 1)

# result = fact(4)
# print(result)

# def fact(n):
#     if n >= 1:
#         return n * fact(n - 1)
#     else: 
#         return 1

# result = int(input("enter integer: "))
# print(fact(result))


def fib(n):
    if n >= 3:
        return fib(n -1) + fib(n - 2)
    return 1

result = int(input("enter integer: "))
print(fib(result))

# def num_ways(n):
#     n = (n -1) + (n - 2)
#     return n

# print(num_ways(4))

# def num_ways(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return num_ways(n-1) + num_ways(n-2)

# print(num_ways(4))