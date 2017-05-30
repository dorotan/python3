# Search for identical data in two dictionaries

dict1 = {
    'a' : 'dog',
    'b' : 'cat',
    'c' : 'guinea pig'
}

dict2 = {
    'a' : 'giraffe',
    'd' : 'leopard',
    'c' : 'guinea pig'
}

# searching for the same keys
k = dict1.keys() & dict2.keys()
print(k)

# searching for the same pairs of keys&values
i = dict1.items() & dict2.items()
print(i)


# searching for keys not included in dict2
k = dict1.keys() - dict2.keys()
print(k)
