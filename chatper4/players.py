players = ["青龙", "白虎", "朱雀", "玄武", "麒麟", "凤凰", "饕餮", "毕方"]
print(players[0:3])
print(players[0:])
print(players[0:-1:2])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])
players2 = players[:]
players.append("黄龙")
players2.append("应龙")
print(players)
print(players2)

players3 = players;
players3.append("獬豸")
players.append("梼杌")
print(players)
print(players3)
