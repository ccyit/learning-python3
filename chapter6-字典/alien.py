# : 后面添加一个空格符合编码规范。
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {'x_position': 0, 'y_position': 25, 'color': 'green', 'points': 5}
print(alien_0)
alien_0['color'] = 'yellow'
print(alien_0)
del alien_0['color']
print(alien_0)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print(favorite_languages)
for name, language in favorite_languages.items():
    print("\nName:" + name.title())
    print("Language:" + language.title())

print()
for name in favorite_languages.keys():
    print(name.title())

print()
for name in sorted(favorite_languages.keys()):
    print(name.title())

print()
for language in set(favorite_languages.values()):
    print(language.title())

