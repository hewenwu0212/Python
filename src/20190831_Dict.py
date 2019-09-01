#-*- coding: UTF-8 -*-
dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
dict1 = { 'abc': 456 }
dict2 = { 'abc': 123, 98.6: 37 }
dict4 = {'Name':'hewenwu','Age':'30','Local':'Shaanxi'}

#访问字典里的值
print(dict4['Name'])

#修改字典
dict4['Name']='Allen'
print(dict4)

#删除字典元素

del dict['Beth']  #删除键
print(dict)
dict1.clear()       #清空字典
print(dict1)

# del dict3   #删除字典
# print(dict3)

#字典的特性
# 键不可变

print(len(dict4))
str1=str(dict4)
print(str1)
str2=dict4.copy()
print(str2)
print(dict1)
print('2:',dict2)

print('4:',dict4)
dict2['abc']=dict4['Name']
print('new2:',dict2)


cities={
    '北京':{
        '朝阳':['国贸','CBD','天阶','我爱我家','链接地产'],
        '海淀':['圆明园','苏州街','中关村','北京大学'],
        '昌平':['沙河','南口','小汤山',],
        '怀柔':['桃花','梅花','大山'],
        '密云':['密云A','密云B','密云C']
    },
    '河北':{
        '石家庄':['石家庄A','石家庄B','石家庄C','石家庄D','石家庄E'],
        '张家口':['张家口A','张家口B','张家口C'],
        '承德':['承德A','承德B','承德C','承德D']
    }
}



for i in cities['北京']:
    print(i)

for i in cities['北京']['朝阳']:
    print(i)

prices = {
    'A': 123,
    'B': 450.1,
    'C': 12,
    'E': 444,
}

max_price = max(zip(prices.values(),prices.keys(),))
print(list(max_price))
print(max_price)



str='asdfghj'
print(str[3])


sites_link = {'runoog':'runoob.com', 'google':'google.com'}
sides = sites_link.keys()
print(sides)

