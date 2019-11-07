dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# dimensions[0] = 200
'''
Traceback (most recent call last):
  File "/Users/user/PycharmProjects/cyc-99-learning-python3/chatper4/dimensions.py", line 4, in <module>
    dimensions[0] = 200
TypeError: 'tuple' object does not support item assignment
'''

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

# 修改元组
dimensions = (400, 100)

print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# 设置代码格式 PEP 8
"""
缩进使用4个空格。
行长：不超过80个字符。
空行：
"""