# 使用任意数量的关键字参数


def build_profile(first, last, **user_info):
    """创建一个字典，包含用户的一些信息"""
    profile = {'first_name': first, 'last_name': last}
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
