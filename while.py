apple_products = ["macbook", "macbook air", "iphone", "ipad", "airpods"]


# we have to initialize the loop with a variable and then increment the loop so that we don't get an infinite loop
index = 0
while index < len(apple_products):
    print(f"{index}: {apple_products[index]}")
    index += 1


# with a for loop there's no need to increment
for product in apple_products:
    print(product)



animals = ["dog", "cat", "parrot", "elephant", 'bird', "horse"]

i = ""
for animal in animals:
    i += animal.upper()
    print(i)


