# 3-1
names = ["xiao ming", "xiao hong", "han meimei"]
print(names[0].title())
print(names[1].title())
print(names[2].title())

# 3-2
print("Hello, " + names[0].title() + "!")
print("Hello, " + names[1].title() + "!")
print("Hello, " + names[2].title() + "!")

# 3-3

transportations = ['火车', '汽车', '飞机', '轮船', '公交车', '自行车']

for transportation in transportations:
    print("I would like to own a " + transportation + ".")

# 3-4
visitors = ["李白", "杜甫", "白居易"]

visitor = visitors.pop()
print(visitor)
visitors.append("陆游")
print(visitors)

visitors.insert(0, "苏轼")
visitors.insert(3, "辛弃疾")
visitors.append("李清照")

print(visitors)
visitor = visitors.pop()
print(visitor)
visitor = visitors.pop()
print(visitor)
visitor = visitors.pop()
print(visitor)
visitor = visitors.pop()
print(visitor)
print(visitors)
del visitors[0]
del visitors[-1]
print(visitors)

