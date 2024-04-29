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

# region    正整数的反转
# num = int(input('num = '))
num = int("12345")
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)
#endregion

# region    《百钱百鸡》问题
# 假设公鸡的数量为x，x的取值范围是0到20
for x in range(0, 21):
    # 假设母鸡的数量为y，y的取值范围是0到33
    for y in range(0, 34):
        z = 100 - x - y
        if 5 * x + 3 * y + z // 3 == 100 and z % 3 == 0:
            print(f'公鸡: {x}只, 母鸡:'
                  f' {y}只, 小鸡: {z}只')
#endregion

# region    CRAPS赌博游戏。
from random import randint

money = 1000
while money > 0:
    print(f'你的总资产为: {money}元')
    go_on = False
    # 下注金额必须大于0小于等于玩家总资产
    while True:
        debt = int(input('请下注: '))
        if 0 < debt <= money:
            break
    # 第一次摇色子
    # 用1到6均匀分布的随机数模拟摇色子得到的点数
    first = randint(1, 6) + randint(1, 6)
    print(f'\n玩家摇出了{first}点')
    if first == 7 or first == 11:
        print('玩家胜!\n')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜!\n')
        money -= debt
    else:
        go_on = True
    # 第一次摇色子没有分出胜负游戏继续
    while go_on:
        go_on = False
        current = randint(1, 6) + randint(1, 6)
        print(f'玩家摇出了{current}点')
        if current == 7:
            print('庄家胜!\n')
            money -= debt
        elif current == first:
            print('玩家胜!\n')
            money += debt
        else:
            go_on = True
print('你破产了, 游戏结束!')
#endregion

# region    斐波那契数列
a, b = 0, 1
for _ in range(20):
    a, b = b, a + b
    print(a)
#endregion

# region    打印100以内的素数
for num in range(2, 100):
    # 假设num是素数
    is_prime = True
    # 在2到num-1之间找num的因子
    for factor in range(2, num):
        # 如果找到了num的因子，num就不是素数
        if num % factor == 0:
            is_prime = False
            break
    # 如果布尔值为True在num是素数
    if is_prime:
        print(num)
#endregion

# region    统计每个英文字母出现的次数
# sentence = input('请输入一段话: ')
sentence = 'aadddvv'
counter = {}
for ch in sentence:
    if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
        counter[ch] = counter.get(ch, 0) + 1
for key, value in counter.items():
    print(f'字母{key}出现了{value}次.')
#endregion

# region    找出股价大于100元的股票并创建一个新的字典
stocks = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
stocks2 = {key: value for key, value in stocks.items() if value > 100}
print(stocks2)
#endregion

# region    案例：统计列表中出现次数最多的三个元素
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]
counter = Counter(words)
# 打印words列表中出现频率最高的3个元素及其出现次数
for elem, count in counter.most_common(3):
    print(elem, count)
#endregion

# region    案例：TopK问题（从序列中找到K个最大或最小元素）
import heapq

list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
# 找出列表中最大的三个元素
print(heapq.nlargest(3, list1))
# 找出列表中最小的三个元素
print(heapq.nsmallest(3, list1))

list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
# 找出价格最高的三只股票
print(heapq.nlargest(3, list2, key=lambda x: x['price']))
# 找出持有数量最高的三只股票
print(heapq.nlargest(3, list2, key=lambda x: x['shares']))
#endregion


# region    案例：itertools - 迭代工具模块，生成各种各样的迭代器
import itertools

# 产生ABCD的全排列
for value in itertools.permutations('ABCD'):
    print(value)

# 产生ABCDE的五选三组合
for value in itertools.combinations('ABCDE', 3):
    print(value)

# 产生ABCD和123的笛卡尔积
for value in itertools.product('ABCD', '123'):
    print(value)

# 产生ABC的无限循环序列
it = itertools.cycle(('A', 'B', 'C'))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
#endregion



















