# Removing duplicates from a sequence & not keeping the order of items
my_list = [98, 1, 2, 3, 3, 5, 6, 9, 9, 3, 1, 0]
my_list2 = [1, 7, 3, 'hello', 'abc']


print(set(my_list))

# output: {0, 1, 98, 3, 2, 5, 6, 9}

print(set(my_list2))

# output: {1, 3, 7, 'hello', 'abc'}


# Removing duplicates from a sequence & keeping the order of items
def reduce_duplicates_from_list(items):
    check = set()
    for item in items:
        if item not in check:
            yield item
            check.add(item)

print(list(reduce_duplicates_from_list(my_list)))

# output: [98, 1, 2, 3, 5, 6, 9, 0]

print(list(reduce_duplicates_from_list(my_list2)))

# output: [1, 7, 3, 'hello', 'abc']
