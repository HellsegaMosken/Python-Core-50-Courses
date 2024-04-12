"""
作者：吕枫烨
创建时间：2024/4/11 17:25
项目：Python-Core-50-Courses
包：
标题：
描述：
"""

print('hello, world')

# region    # ------------ 判断变量类型 ------------
a = 100
b = 12.345
c = 'hello, world'
d = True
print(type(a))    # <class 'int'>
print(type(b))    # <class 'float'>
print(type(c))    # <class 'str'>
print(type(d))    # <class 'bool'>
# endregion

# region    # ------------ 变量类型转换 ------------
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
# endregion

# region    # ------------ 算术运算 ------------

print(321 + 123)     # 加法运算
print(321 - 123)     # 减法运算
print(321 * 123)     # 乘法运算
print(321 / 123)     # 除法运算
print(321 % 123)     # 求模运算
print(321 // 123)    # 整除运算
print(321 ** 123)    # 求幂运算
# endregion

# region    # ------------ 赋值运算符 ------------

a = 10
b = 3
a += b        # 相当于：a = a + b
a *= a + 2    # 相当于：a = a * (a + 2)
print(a)      # 算一下这里会输出什么
# endregion

# region    # ------------ 比较运算符和逻辑运算符 ------------

flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not (1 != 2)
print('flag0 =', flag0)    # flag0 = True
print('flag1 =', flag1)    # flag1 = True
print('flag2 =', flag2)    # flag2 = False
print('flag3 =', flag3)    # flag3 = False
print('flag4 =', flag4)    # flag4 = True
print('flag5 =', flag5)    # flag5 = False
# endregion

# region    例子1：华氏温度转换为摄氏温度。
f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')
# endregion

# region    例子2：输入圆的半径计算计算周长和面积。
radius = float(input('请输入圆的半径: '))
perimeter = 2 * 3.1416 * radius
area = 3.1416 * radius * radius
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)
# endregion

# region    例子3：输入年份判断是不是闰年。
year = int(input('请输入年份: '))
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(is_leap)
# endregion

# region    # ------------ if语句的使用 ------------

username = input('请输入用户名: ')
password = input('请输入口令: ')
# 用户名是admin且密码是123456则身份验证成功否则身份验证失败
if username == 'admin' and password == '123456':
    print('身份验证成功!')
else:
    print('身份验证失败!')

x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print(f'f({x}) = {y}')
# endregion

# region    # 例子1：英制单位英寸与公制单位厘米互换。

value = float(input('请输入长度: '))
unit = input('请输入单位: ')
if unit == 'in' or unit == '英寸':
    print('%f英寸 = %f厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
    print('%f厘米 = %f英寸' % (value, value / 2.54))
else:
    print('请输入有效的单位')
# endregion

# region    # 例子2：百分制成绩转换为等级制成绩。
# score = float(input('请输入成绩: '))
score = 90
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('对应的等级是:', grade)
# endregion

# region    # 例子3：输入三条边长，如果能构成三角形就计算周长和面积。

# a = float(input('a = '))
# b = float(input('b = '))
# c = float(input('c = '))
a = float(1.2)
b = float(1.5)
c = float(1)
if a + b > c and a + c > b and b + c > a:
    peri = a + b + c
    print(f'周长: {peri:.2f}')
    half = peri / 2
    area = (half * (half - a) * (half - b) * (half - c)) ** 0.5
    print(f'面积: {area:.2f}')
else:
    print('不能构成三角形')
# endregion

# region    # ------------ for-in循环 ------------

total = 0
for x in range(1, 101):
    total += x
print(total)

total = 0
for x in range(2, 101, 2):
    total += x
print(total)
# endregion

# region    # ------------ while循环 ------------

import random

# 产生一个1-100范围的随机数
answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入: '))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('恭喜你猜对了!')
        break
# 当退出while循环的时候显示用户一共猜了多少次
print(f'你总共猜了{counter}次')
# endregion

# region    # ------------ 嵌套的循环结构 ------------

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i}*{j}={i * j}', end='\t')
    print()
# endregion

# region    例子1：输入一个正整数判断它是不是素数。

num = int(input('请输入一个正整数: '))
end = int(num ** 0.5)
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print(f'{num}是素数')
else:
    print(f'{num}不是素数')
# endregion

# region    例子2：输入两个正整数，计算它们的最大公约数和最小公倍数。

# x = int(input('x = '))
# y = int(input('y = '))
x = int(3)
y = int(9)
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print(f'{x}和{y}的最大公约数是{factor}')
        print(f'{x}和{y}的最小公倍数是{x * y // factor}')
        break
# endregion
















