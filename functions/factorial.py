def fact(n):
    if n >= 1:
        return n * fact(n - 1)
    else:
        return 1

result = int(input("enter the integer to check its factorial: "))
print(fact(result))