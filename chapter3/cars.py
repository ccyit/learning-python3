cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()
print(cars)

cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort(reverse=True)
print(cars)

cars = ["bmw", "audi", "toyota", "subaru"]
print("Here is the original list:")
print(cars)
print("Here is the sorted list:")
print(sorted(cars, reverse=True))
print("Here is the original list again:")
print(cars)

# 倒着打印列表
cars.reverse()
print(cars)
# 确定列表的长度
print(len(cars))

