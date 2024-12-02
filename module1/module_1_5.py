print('Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи"')

#2
immutable_var = 1, 'tuple', False
print('\n2. Immutable tuple:',immutable_var)
#immutable_var[0] = 5
#print(immutable_var)

#3
print('\n3. Изменение значений в кортеже вызовет ошибку,'
      '\nпоскольку, кортеж - неизменяемый список.'
      '\nДанные можно менять в кортеже, только если'
      '\nдобавить в него элементы списка')
mutable_tuple_list = [True, 8], 'str'
print('\n4. Mutable tuple-list :',mutable_tuple_list)
mutable_tuple_list[0][1] = 49
print('Mutable tuple-list :',mutable_tuple_list)
mutable_tuple_list[0][0] = 49
#mutable_list[1] = 49 - TypeError: 'tuple' object does
#not support item assignment
mutable_list = ['результат', 543, True]
print('\nMutable list :',mutable_list)
mutable_list[0] = 800
mutable_list[1] = False
mutable_list[2] = 'изменен'
print('Mutable list :',mutable_list)
