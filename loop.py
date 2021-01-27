# initiliaze the x variable
# x = 0

# # create a range from 10 to 20 inclusive
# for num in range(10, 21):
# # chack if the number is odd
#     if num % 2 != 0:
# # add to variable x
#         x += num
# # print result
#         print(f"num is {num} and x is {x}")


# sentences = int(input("how many times do you want to repeat it? "))

# for sentence in range(sentences):
#     print("read a book")


# for num in range(1, 21):
#     if num % 2 == 0:
#         print(f"{num} is even.")
#     elif num == 4 or num == 13:
#         print(f"{num} is unlucky.")
#     else:
#         print(f"{num} is odd.")
   
# for x in range(3):
#     for _ in range(1, 11):
#         print('*' * _)

# for i in range(1, 11):
#     count = 1
#     stars = ""
#     while count < i:
#         stars += "*"
#         count += 1
#     print(stars)
    

from random import randint

num = 0
n = 0

while num == 5:
    n += 1
    num = randint(1, 10)
    print(num)
