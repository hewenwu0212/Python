#-*- coding: UTF-8 -*-

parame = {1,2,3,4,1,5}
parame2 = {1,2,6}
print(parame)
print(1 in parame)
print(parame-parame2)
print(parame|parame2)
print(parame&parame2)
print(parame^parame2)
a = {x for x in 'asdagsdgdrgdfgh' if x not in 'abc'}
print(a)

#集合的基本操作
#1、添加元素
thisset = set(("Google", "Runoob", "Taobao"))
thisset.add('Twitter')
print(thisset)
# thisset.update('Facebook')
print(thisset)
thisset.update({1,3})
print(thisset)
#2、移除元素
#s.remove(x)
#s.discard(x)   如果元素不存在，不会报错
#s.pop() 随即删除元素
#remove
thisset.remove('Runoob')
print(thisset)

#discard
thisset.discard('Runoob')
print(thisset)

#pop
thisset_del = thisset.pop()
print(thisset_del)

#3、计算集合中元素个数
print(len(thisset))
print(thisset)
thisset1 = set(("Google", "Runoob", "Taobao"))
print(len(thisset1))
print(thisset1)


#4、清空集合
#s.clear()
thisset1.clear()
print(thisset1)

#5、判断元素是否在集合中存在
# x in set

thisset2 = set(("Google", "Runoob", "Taobao"))
if ('Google' in thisset2):
    print('in')
else:
    print('out')
