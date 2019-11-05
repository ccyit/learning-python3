# 传递列表


def greet_user(name):
    """简单的问候语。"""
    msg = "Hello, " + name.title() + "!"
    print(msg)


def greet_users(names):
    """向列表的每位用户都发出简单的问候语。"""
    for name in names:
        greet_user(name)


user_names = ['hannah', 'ty', 'margot']
greet_users(user_names)
