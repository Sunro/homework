#2. Работа со словарями:
#- Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение.
#  Например: Имя(str)-Год рождения(int).
my_dict = {'Andrey':1980,'Grigory':1984,'Nikolay':1992}
#- Выведите на экран словарь my_dict.
print('Dict:',my_dict)
#- Выведите на экран одно значение по существующему ключу, одно по отсутствующему из словаря my_dict без ошибки.
print('Existing value:',my_dict['Andrey'])
print('Not existing value: ',my_dict.get('Kamila'))
#- Добавьте ещё две произвольные пары того же формата в словарь my_dict.
my_dict.update({'Vladimir':1988,'Alena':1989})
#- Удалите одну из пар в словаре по существующему ключу из словаря my_dict и выведите значение из этой пары на экран.
                # del my_dict['Andrey']
print('Deleted value:',my_dict.pop('Andrey'))
                #print('Not existing value:',my_dict.get('Andrey'))
#- Выведите на экран словарь my_dict.
print('Modified dictionary:',my_dict)

#3. Работа с множествами:
#  - Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.
my_set = {5, True, 'Апельсин', 9, 109.5, 9, True}
print(f'\n\n\nSet:',my_set)
                #list = {5, True, 'String', 9, 109.5, 9, True}
    #my_set = set(list)
#  - Выведите на экран множество my_set (должны отобразиться только уникальные значения).
                # print(f'add(5,3)',my_set.add((5,3)))
my_set.add((5,3))
#  - Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
#  - Удалите один любой элемент из множества my_set.
                # print(f'Discard 3',my_set.discard(3))
my_set.discard(3)
                # print(f'my_set',my_set)
                # print(f'Discard 9',my_set.discard(9))
my_set.discard(9)
#  - Выведите на экран измененное множество my_set.
print(f'Modified set:',my_set)

