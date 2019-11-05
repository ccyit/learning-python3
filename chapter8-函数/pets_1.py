# 默认值参数, 先列出没有默认值的参数，再列出有默认只的参数，
# python可以正确的解读位置参数


def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


# 函数有多种调用方式
describe_pet(pet_name='willie')
describe_pet('willie')
describe_pet('harry', 'hamster')
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')
