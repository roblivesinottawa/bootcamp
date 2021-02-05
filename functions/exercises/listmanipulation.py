def list_manipulation(_list, command, location, value=None):
  
    if command == "remove" and location == "end":
        return _list.pop(-1)
    elif command == "remove" and location == "beginning":
        return _list.pop(0)
    elif command == "add" and location == "beginning":
        return _list.insert(0,value)
    elif command == "add" and location == "end":
        return _list.append(value)

l  = [1,2,3]
com = input("type 'remove' or 'add': ")
loc = input("type 'end' or 'beginning': ")
val = int(input("enter a value: "))
print(list_manipulation(l, com, loc))