"""
作者：吕枫烨
创建时间：2024/4/11 17:25
项目：Python-Core-50-Courses
包：
标题：
描述：
"""

print('hello, world')

a = 45          # 变量a保存了45
b = 12          # 变量b保存了12
print(a + b)    # 57
print(a - b)    # 33
print(a * b)    # 540
print(a / b)    # 3.75

a = 100
b = 12.345
c = 'hello, world'
d = True
print(type(a))    # <class 'int'>
print(type(b))    # <class 'float'>
print(type(c))    # <class 'str'>
print(type(d))    # <class 'bool'>

a = 100
b = 12.345
c = 'hello, world'
d = True
# 整数转成浮点数
print(float(a))    # 100.0
# 浮点型转成字符串 (输出字符串时不会看到引号哟)
print(str(b))      # 12.345
# 字符串转成布尔型 (有内容的字符串都会变成True)
print(bool(c))     # True
# 布尔型转成整数 (True会转成1，False会转成0)
print(int(d))      # 1
# 将整数变成对应的字符 (97刚好对应字符表中的字母a)
print(chr(97))     # a
# 将字符转成整数 (Python中字符和字符串表示法相同)
print(ord('a'))    # 97



