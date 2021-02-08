# lambda functions take one single operation

_list = [1,2,3,4,5,6]

grab_evens = list(filter(lambda n: n % 2 == 0, _list))
print(grab_evens)

grab_odds = list(filter(lambda num: num % 2 != 0, _list))
print(grab_odds)


names = ['Johnson', 'Jeremy', 'Mary', 'Jebediah']

j_names = list(filter(lambda n: n[0] == "j".upper(), names))

print(j_names)