from chapter9.car import Car


class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类的属性,再初始化电动汽车特有的属性"""
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def fill_age_tank(self):
        """电动汽车没有油箱"""
        print("This car doesn't need a gas tank!")


if __name__ == '__main__':
    my_tesla = ElectricCar('tesla', 'model s', 2016)
    print(my_tesla.get_descriptive_name())
    my_tesla.describe_battery()
    my_tesla.fill_age_tank()