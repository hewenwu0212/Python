#-*- coding: UTF-8 -*-
tup1=(1,2,3,4,5)
tup2=('Google', 'Runoob', 1997, 2000);
tup3="a", "b", "c", "d";                 #  不需要括号也可以

print(type(tup3))
tup4=(1)                #元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用：
tup5=(1,)
print(type(tup4))
print(type(tup5))

#访问元组
#元组可以使用下标索引来访问元组中的值，
print(tup1[0])
print(tup2[2])
print(tup3[1:4])

#修改元组
#元组中的元素值是不允许修改的，但我们可以对元组进行连接组合。
tup6=(1,2,3,4,5)
tup7="a", "b", "c", "d";
tup8=tup6+tup7
print(tup8)


# 删除元组
# 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组。

del tup8
# print(tup8)

# 删除元组之后报错：
# NameError: name 'tup8' is not defined

#元组运算符
print(len(tup3))
print(tup1+tup2)
print(tup1*3)
if (3 in tup1):
    print('ok')
else:
    print('no')

#元组索引，截取
print(tup2[2])
print(tup3[2])
print(tup3[2:])
print(max(tup1))
print(min(tup1))
list1= ['Google', 'Taobao', 'Runoob', 'Baidu']
print(list1)
tp_list1=tuple(list1)
list_tp=list(tp_list1)
print(tp_list1)
print(list_tp)