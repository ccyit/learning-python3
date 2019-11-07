cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

age = 20
if 18 <= age <= 40:
    print("年龄在18到40岁之间。")

age = 55
if age < 18 or age > 40:
    print("年龄小于18或者大于40。")

year = 2100
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("{} 年是闰年。".format(year))
else:
    print("{} 年不是闰年。".format(year))


salary = 5000
if salary < 5000:
    print("不用交税")
elif salary < 10000:
    print("需要交很少税")
elif salary < 50000:
    print("需要交很多税")
else:
    pass

empty_list = []
if empty_list:
    pass
