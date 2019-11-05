def build_person(first_name, last_name, age=''):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', age=27)
print(musician)


# 吉米·亨德里克斯（James Marshall "Jimi" Hendrix，1942年11月27日-1970年9月18日），
# 出生于美国华盛顿州西雅图，美国吉他手、歌手、作曲人，被公认为是摇滚音乐史中最伟大的电吉他演奏者。
# 1966年吉米组建乐队，1967年夏，他成功地进行了欧洲巡演，在保罗·麦卡特尼的大力推荐下，
# 他参加了伍德斯托克音乐节，他的成功使他跻身于世界明星的行列。
