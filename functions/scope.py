# if the variable name is placed outside of the function, it can be accessed by other functions.
# if the variable name is placed inside the function, then only that function can access the variable

def sayhi():
    name = "Tony Stark"
    return f"hello mr.{name}"


print(sayhi())

# def happybirthday():
#     return f"happy birthday mr.{name}" #undefined

# print(happybirthday())

total = 0
def increment():
    global total
    total += 1
    return total

print(increment())


