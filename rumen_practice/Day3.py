my_list = ['aaa','bbb','ccc','ddd']
for i in my_list:
    print(i)

my_list.append('eee')
print(my_list)

print(my_list.extend([1,2,3]))


# 分配办公室
import random
# 定义办公室列表
offices = [[],[],[]]

# 定义老师列表
teachers = ['A','B','C','D','E','F','G','H']

# 产生随机数，决定老师去哪个办公室
for teacher in teachers:
    result = random.randint(0,2)
    offices[result].append(teacher)
# 输出分配结果
print(offices)

for office in offices:
    print(f'该办公室共有老师{len(office)}名，老师名字为：')
    for teacher in office:
        print(teacher,end = ' ')
    print() # 为了换行，美观