"""
作者：吕枫烨
创建时间：2024/4/12 16:34
项目：Python-Core-50-Courses
包：
标题：
描述：
"""

# region    华氏温度转换为摄氏温度。
f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')
# endregion

# region    入圆的半径计算计算周长和面积。
radius = float(input('请输入圆的半径: '))
perimeter = 2 * 3.1416 * radius
area = 3.1416 * radius * radius
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)
# endregion

# region    输入年份判断是不是闰年。
year = int(input('请输入年份: '))
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(is_leap)
# endregion

# region    英制单位英寸与公制单位厘米互换。

value = float(input('请输入长度: '))
unit = input('请输入单位: ')
if unit == 'in' or unit == '英寸':
    print('%f英寸 = %f厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
    print('%f厘米 = %f英寸' % (value, value / 2.54))
else:
    print('请输入有效的单位')
# endregion

# region    百分制成绩转换为等级制成绩。
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

# region    输入三条边长，如果能构成三角形就计算周长和面积。

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

# region    找出所有水仙花数

for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)
# endregion






