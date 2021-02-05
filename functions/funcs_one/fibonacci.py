def fib(num):
    if num >= 3:
        return fib(num - 1) + fib(num - 2)
    return 1


result = int(input("enter integer: "))
print(fib(result))

