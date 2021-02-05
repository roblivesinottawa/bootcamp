def compact(_list):
    return [x for x in _list if x]

print(compact([0,1,2,"", [], False, {}, None, "All done"]))

def compact1(list_):
    truthy = []
    for x in list_:
        if x: truthy.append(x)
    return truthy
   

print(compact1([0,1,2,"", [], False, {}, None, "All done"]))