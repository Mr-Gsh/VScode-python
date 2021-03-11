'''
            注释
'''


#python的单行注释，使用 # 符号
print("Hello World!")

# ""   ''  都可以

print('Hello World!')

'''
多行注释  三个单引号/双引号 都可以
'''

# 快捷键 ctrl+/





'''
变量类型 ：1.int 整型
          2.float 浮点型，可以有小数点
          3.bool 布尔型 
          4.String 字符串 
          5.List 列表
          6.Tuple 元组
          7.Dictionary 字典
'''



# 查看类型 type()函数  <class 'int'>
num1 = 10
print(type(num1))  #行内注释空两格
name = '小明'

'''
            输出
'''

# 占位符 方法一
# print('%s今年%d岁' % name %num1)  这样写是错误的，正确如下
print('%s今年%d' % (name,num1))

# %f 默认保留六位小数
# %.nf 保留n位小数
high = 170
print('身高为%f' % high)
print('身高为%.1f' % high)

# 方法二 f-String，使用{}占位

print(f'{name}今年{num1}岁，身高为{high}')  #python3.6+版本支持


# print默认加一个换行符 \n  可以修改
print('Hello',end = ' ')



'''
            输入
'''
# input()输入的内容，回车后得到的全部都是string类型

'''
            运算符
'''
# 算数运算符

#  + - * / 
#  // 整除(求商)
#  % 取余数
#  ** 指数,幂运算
#  () 可以改变优先级



# 从键盘上录入苹果的价格、重量，输出：苹果单价9.00元/斤，购买了5.00斤，需要支付45.00元.

# print('水果支付价格计算，请输入苹果的价格：')
# price = input()     等价于

price = input('水果支付价格计算\n请输入苹果的价格：')
weight = input('重量：')
# result = price*weight   报错can't multiply sequence by non-int of type 'str'
# result = float (price*weight)  报错can't multiply sequence by non-int of type 'str'
result = float(price) * float(weight)
print(f'苹果单价{price}元/斤，购买了{weight}斤，需要支付{result}元')