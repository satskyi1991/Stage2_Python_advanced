
dict = {
        'Ukraine':'Kiev',
        'Germany': 'Berlin',
        'France': 'Paris',
        'Italy':'Rome',
}

print(dict)
myList = ['Ukraine', 'Spain', 'Poland', 'Germany', 'Italy', 'France', 'Russia', 'Turkey']

for elem in (myList):
    # print(elem)
    if elem in dict:
        print (dict[elem])