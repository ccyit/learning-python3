# 位置参数的顺序很重要。
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# 关键字参数,指定函数定义是参数的名字。
describe_pet(pet_name='harry', animal_type='hamster')



