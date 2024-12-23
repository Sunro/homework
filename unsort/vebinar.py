#a = 97
#b = 98

a = 'hello'
print(a[:2])
print(a[-1])
#[start:end:step]
print(a[::-1])
b = a + "g"
a = 'a'
b = 'b'
print(a>b)
#masive
a = [1,2,3,4,5]
print(a)

# apper верхний регистр
#a.lower()
#a.find('e')
a = 'World' #r = k
str1 = a[:2]
str2= a[3:]
#a = str1+ 'k' +str2
print(a)
a = a.replace('r','k')
print(a)

#список - коллекция элементов
a = [1,2,3,4]
a.remove(2)
print(a)
a.clear() #очистка

#massive
a = [[1,2],[2,3]]
print(a[0][0])
#четырехмерные массивы бессмыленны

a = [1,2,3]
b= a.pop()
print(b,a)
a.sort()#пузырьковая - медленная
a.reverse()

#словари - хешфункция ключ-значение "key":"value"
dict1 = {1:"a",2:"b",3:"c"}
print(dict1.keys())
print(dict1.values())
dict1[4]= "d"
print(dict1)
del dict1[4]

#множества - упорядоченное количество уникальных элементов, математическая абстракция
set1 = {1,2,2,4,1,1,5,True,False}
print(set1)
#del set1[0]
set1.remove(1)

set1 = {1,2,3}
set2= {4,2,5}
union_set = set1|set2
print(union_set)
inter_set = set1&set2 #- пересечение множеств
diff_set = set1 - set2
print(diff_set)