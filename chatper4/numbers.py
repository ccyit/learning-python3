for value in range(1, 5):
    print(value)

numbers = list(range(1, 6))
print(numbers)

# 偶数列表
even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

# 不实用临时变量 square
squares = []
for value in range(1, 11):
    # square = value ** 2
    squares.append(value ** 2)
print(squares)

digits = list(range(10))
print(digits)
print(min(digits))
print(max(digits))
print(sum(digits))

squares = [x ** 2 for x in range(1, 11)]
print(squares)


