# Дополнительное практическое задание по модулю: "Подробнее о функциях."

# Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности
# Задание "Раз, два, три, четыре, пять .... Это не всё?":
# Наши студенты, без исключения, - очень умные ребята. Настолько умные, что иногда по утру
# сами путаются в том, что намудрили вчера вечером.
# Один из таких учеников уснул на клавиатуре в процессе упорной учёбы (ещё и трудолюбивые).
# Тем не менее, даже после сна, его код остался рабочим и выглядел следующим образом:

# data_structure = [
#   [1, 2, 3],
#   {'a': 4, 'b': 5},
#   (6, {'cube': 7, 'drum': 8}),
#   "Hello",
#   ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]

# Увидев это студент задался вопросом: "А есть ли универсальное решение для подсчёта суммы всех чисел и длин всех строк?"
# Да, выглядит страшно, да и обращаться нужно к каждой внутренней структуре (списку, словарю и т.д.) по-разному.
# Ученику пришлось каждый раз использовать индексацию и обращение по ключам - универсального решения
# для таких структур он не нашёл.

# Помогите сокурснику осуществить его задумку.
# Что должно быть подсчитано:
# Все числа (не важно, являются они ключами или значениям или ещё чем-то).
# Все строки (не важно, являются они ключами или значениям или ещё чем-то)
# Для примера, указанного выше, расчёт вёлся следующим образом:
# 1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99

# Входные данные (применение функции):
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
dict_to_list = []
tuple_to_list = []
list_to = []
data_structure_convert_to_list = []
def calculate_structure_sum(*data):
  all_convert = 0
  for i in data:
    uni_list = []
    if isinstance(i, list):

      # print('list', i)
      if len(i) > 1:
        for j in i:
          if not isinstance(j, int or str):
            calculate_structure_sum(j)
            # print('test-list',j)
          else:
            list_to.append(i)

    if isinstance(i, dict):
      dict_to_list.append(list(i))
      k = list(i.values())
      data_structure_convert_to_list.append(j)
      data_structure_convert_to_list.append(k)
      # print('dict', i)
      # list_ = list(i)
      # len_list = list(i.values())
      # for j in list_:
      #   len_list.append(len(j))
      # print('sum_dict', len_list)
      # print('dict', i)
      for j in i:
        if not isinstance(j, int or str):
          calculate_structure_sum(j)
          # print('test-dict', j)
        else:
          data_structure_convert_to_list.append(j)
        if not isinstance(k, int or str):
          calculate_structure_sum(k)
          # print('test-dict', j)
        else:
          data_structure_convert_to_list.append(k)

    # if isinstance(i, str):
    #   # print('str', i)
    #   data_structure_convert_to_list.append(i)
    #   # print('str', i)
    #   # print('len_str', i, len_str)

    if isinstance(i, tuple):
      # print('tuple', i)
      # # len_tuple = sum(i)
      # # len_str.append(len(i))
      # # print(len_tuple)
      # len_tuple = []
      # no_int_tuple = []
      # for j in i:
      #   if isinstance(j, int):
      #     # len_tuple += j
      #     len_tuple.append(j)
      #   else:
      #     no_int_tuple.append(j)
      # print('tuple', i)
      if len(i) > 1:
        for j in i:
          if not isinstance(j, int or str):
            calculate_structure_sum(j)
            print('test-tuple', j)
          else:
            tuple_to_list.append(list(i))
      # print('len_tuple', len_tuple)
      # print('no_int_tuple', no_int_tuple)
      # if range(no_int_tuple) != 0:
        #   calculate_structure_sum(*j)
      # print('len_tuple', len_tuple)
  data_structure_convert_to_list.append(list)
  data_structure_convert_to_list.append(tuple_to_list)
  data_structure_convert_to_list.append(tuple_to_list)

# numbers = (10, 20, 30, 40, 50)
# total = sum(numbers)
# print(total)  # Выведет: 150 (сумма всех чисел в кортеже) [1](https://ru.hexlet.io/qna/python/questions/kakaya-funktsiya-nuzhna-dlya-slozheniya-chisle-v-python)


# result = calculate_structure_sum(*data_structure)
calculate_structure_sum(*data_structure)
print('list_unpack')
print(list(data_structure))
# print(result)
print(data_structure_convert_to_list)

# Выходные данные (консоль):
# 99

# Примечания (рекомендации):
# Весь подсчёт должен выполняться одним вызовом функции.
# Рекомендуется применить рекурсивный вызов функции, для каждой внутренней структуры.
# Т.к. каждая структура может содержать в себе ещё несколько элементов, можно использовать параметр *args
# Для определения типа данного используйте функцию isinstance.
