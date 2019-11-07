alien_1 = {'color': 'green', 'point': 5}
alien_2 = {'color': 'red', 'point': 15}
alien_3 = {'color': 'blue', 'point': 25}

aliens = [alien_1, alien_2, alien_3]
print(aliens)

# 字典列表，列表里面添加字典。
aliens = []
for i in range(30):
    aliens.append({'color': 'green', 'point': 5})

for alien in aliens[:5]:
    print(alien)
print("...")
print(len(aliens))

# 字段中存储列表。
