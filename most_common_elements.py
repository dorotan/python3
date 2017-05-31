from collections import Counter
# Specifying the most common elements in a sequence

animals = ['guinea pig', 'dog', 'cat', 'guinea pig', 'dog',
           'parrot', 'turtle', 'guinea pig', 'cat'
           'guinea pig', 'turtle', 'bird', 'dog', 'parrot',
           'guinea pig', 'bird', 'guinea pig', 'dog',
           'parrot', 'cat', 'guinea pig'
           'dog', 'cat', 'cat', 'dog', 'cat', 'turtle']

animals_count = Counter(animals)
top_three = animals_count.most_common(3)

print(top_three)

# output: [('guinea pig', 5), ('dog', 5), ('cat', 5)]
