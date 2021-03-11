# 注释
python的单行注释，使用 # 符号

多行注释  三个单引号/双引号 都可以

单行注释快捷键 ctrl+/  

# 变量
1.int 整型
2.float 浮点型，可以有小数点
3.bool 布尔型 
4.String 字符串 
5.List 列表
6.Tuple 元组
7.Dictionary 字典

# 输入 
input()输入的内容，回车后得到的全部都是string类型
```
name = input('请输入名字：')
```

# 输出
## 方法一
`print('%s今年%d岁' % name %num1)`  
这样写是错误的，正确如下
`print('%s今年%d' % (name,num1))`

 %f 默认保留六位小数
 %.nf 保留n位小数
```
high = 170
print('身高为%f' % high)
print('身高为%.1f' % high)
```

## 方法二
f-String，使用{}占位
`print(f'{name}今年{num1}岁，身高为{high}')  #python3.6+版本支持`

print默认加一个换行符 \n  可以修改
`print('Hello',end = ' ')`

# 运算符
算术运算符
+-*/
  // 整除(求商)
  % 取余数
 ** 指数,幂运算
  () 可以改变优先级