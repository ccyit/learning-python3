# 4-1
pizzas = ['茄子', '辣椒', '土豆']
for pizza in pizzas:
    print("I like %s pizza." % pizza)
print("I really like pizza!")

# 4-2
pets = ["dog", 'cat', 'pig']
for pet in pets:
    print("A {} would make a great pet.".format(pet))
print("Any of these animals would make a great pet!")

# 4-3
for i in range(1, 21):
    print(i, end=" ")

# 4-4
for i in range(1, 11):
    print(i, end=" ")
print()
# 4-5
numbers = list(range(1, 1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 4-6
odd_list = list(range(1, 20, 2))
for odd in odd_list:
    print(odd, end=" ")
print()

# 4-7
three_list = list(range(3, 31, 3))
for three in three_list:
    print(three, end=" ")
print()

# 4-8
tubes = [x ** 3 for x in range(1, 11)]
for x in tubes:
    print(x, end=" ")
print()

# 4-9
squares = [x ** 2 for x in range(1, 11)]
print(squares)

# 4-10