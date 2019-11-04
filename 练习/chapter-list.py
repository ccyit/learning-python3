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
print(len(visitors))

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

visitor = "李白"
visitors.append(visitor)
visitors.append(visitor)
visitors.insert(1, "杜甫")
print(visitors)

visitors.remove(visitor)
print(visitors)
visitors.remove(visitor)
print(visitors)

# 3-8
cities = ["北京", "上海", "广州", "深圳", "杭州"]
print(cities)
print(sorted(cities))
print(sorted(cities, reverse=True))
cities.reverse()
print(cities)

cities.reverse()
print(cities)

cities.sort()
print(cities)

cities.sort(reverse=True)
print(cities)

# 3-9
print(len(visitors), visitors)
# 3-10
# 编程语言排序
programming_languages = ["Python", "C", "Java", "JavaScript", "Ruby", "Swift",
                         "Objective-C", "C++", "HTML5", "Go", "PHP"]
print(programming_languages)
print(sorted(programming_languages))
print(sorted(programming_languages, reverse=True))
programming_languages.sort()
print(programming_languages)
programming_languages.sort(reverse=True)
print(programming_languages)
programming_languages.reverse()
print(programming_languages)
programming_languages.reverse()
print(programming_languages)

print(len(programming_languages))

# 3-11
# print(programming_languages[11])
print(programming_languages[-1])
'''
Traceback (most recent call last):
  File "/Users/user/PycharmProjects/cyc-99-learning-python3/练习/chapter-list.py", line 95, in <module>
    print(programming_languages[11])
IndexError: list index out of range
'''

