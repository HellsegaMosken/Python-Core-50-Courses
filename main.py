"""
作者：吕枫烨
创建时间：2024/4/11 17:25
项目：Python-Core-50-Courses
包：
标题：
描述：
"""

# region    # ------------ print ------------
print('%.1f华氏度 = %.1f摄氏度' % (f, c))
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')
# endregion

# region    # ------------ if ------------
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print(f'f({x}) = {y}')
# endregion

# region    # ------------ for ------------
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


