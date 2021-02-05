"""define a function called frequency
    pass a list and a search term as parameter(primitive value)
    return the number of times the search_term appears in the list
"""
# to solve this, use the count method and pass search_item as the argument


def frequency(_list, search_item):
    return _list.count(search_item)

answer = frequency([1,2,3,4,5,6,3,4,5,2,5,6], 4)
print(f"the number of times the item appears in the list is: {answer}")

