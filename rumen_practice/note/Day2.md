# if 判断语句
## If 判断的基本格式

```python
if 判断条件:
    判断条件为 True,会执行的代码
    判断条件为 True,会执行的代码
    ...

顶格书写的代码,代表和 if 判断没有关系
在 python 中使用缩进,代替代码的层级关系, 在 if 语句的缩进内,属于 if 语句的代码块(多行代码的意思)
```

## if else 结构

```python 
if 判断条件:
    判断条件为 True,会执行的代码
    判断条件为 True,会执行的代码
    ...
else:
    判断条件为 False, 会执行的代码
    判断条件为 False, 会执行的代码
    .....
    
    
if 和 else 只会执行其中的一个   
```

## if elif 结构

```python 
if 	判断条件1:
    判断条件1成立,执行的代码
elif 判断条件2:
    判断条件1不成立,判断条件2 成立,会执行的代码
else:
    判断条件1和判断条件2都不成立,执行的代码
    
--------
if 判断条件1:
    判断条件1成立执行的代码
    
if 判断条件2:
    判断条件2 成立执行的代码
```

##  if 嵌套

```python
if 判断条件1:
    判断条件1 成立,会执行的代码
    if 判断条件2:
        判断条件1成立, 判断条件2成立执行的代码
    else:
        判断条件1成立, 判断条件2不成立执行的代码
else:
    判断条件1不成立,会执行的代码
```

## 三目运算
```python 
if 判断条件1:
    表达式1
else:
    表达式2
    
判断条件成立,执行表达式 1, 条件不成立,执行表达式 2

变量 = 表达式1 if 判断条件 else 表达式2  # 推荐使用扁平化代码

变量最终存储的结构是: 
    判断条件成立,表达式1的值, 
    条件不成立,表达式2的值
```

#  循环
## while 循环
```python 
while 判断条件:
    判断条件成立,执行的代码
    判断条件成立,执行的代码
    
不在 while 的缩进内,代表和循环没有关系    

```
## for 循环
```python
for 变量 in 字符串:
    代码
for 循环也称为 for 遍历,会将字符串中的字符全部取到    
```

## Break 和 continue

```python
1. break 和 continue 是 python 两个关键字
2. break 和 continue 只能用在循环中
3. break 是终止循环的执行, 即循环代码遇到 break,就不再循环了
   continue 是结束本次循环,继续下一次循环, 即本次循环剩下的代码不再执行,但会进行下一次循环
```