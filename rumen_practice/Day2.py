# test1
age = input('请输入年龄：') # 这里是str型
# if age >= 18:
#     print('满足18岁，可以进入网吧')
age = int(age)

if age >= 18:
    print('满足18岁，可以进入网吧')
print('判断结束')


# test2
age = input('请输入年龄：') 
age = int(age)
if age >= 18:
    print('满足18岁，可以进入网吧')
else:
    print('不满足18岁，回去好好学习')
print('判断结束')


# test3
score = input('请输入您的成绩：')
score = int(score)
if score >= 90:
    print('优秀')
elif score >=80 and score < 90:
    print('良好')
elif score >= 60:
    print('及格')
else:
    print('不及格')

# test4
import random
user = int(input('请输入要出的拳（1）剪刀，（2）石头，（3）布：'))  
computer = random.randint(1,3)  # 产生 [a, b] 之间的随机整数,包含 a 和 b
print('电脑出的是 %d' %computer)
if user == computer:
    print('平局')
elif (user == 1 and computer == 2) or (user == 2 and computer == 3) or (user == 3 and computer == 1):
    print('你输了')
else:
    print('你赢了')

# test5
a = int(input('请输入A的值：'))
b = int(input('请输入B的值：'))

result = a-b if a > b else b-a
print(result)

