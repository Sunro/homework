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

def calculate_structure_sum(*data):
  for i in data:
    uni_list = []
    if isinstance(i, list):
      print('list', i)
      # if len(i) > 1:
      #   for j in i:
      #     if not isinstance(j, list):
      #       calculate_structure_sum(j)
      #     print('test')

    if isinstance(i, dict):
      print('dict', i)
      list_ = list(i)
      len_list = list(i.values())
      for j in list_:
        len_list.append(len(j))
      # print('sum_dict', len_list)

    if isinstance(i, str):
      print('str', i)
      len_str = []
      len_str.append(len(i))
      # print('str', i)
      # print('len_str', i, len_str)

    if isinstance(i, tuple):
      print('tuple', i)
      # len_tuple = sum(i)
      # len_str.append(len(i))
      # print(len_tuple)
      len_tuple = []
      no_int_tuple = []
      for j in i:
        if isinstance(j, int):
          # len_tuple += j
          len_tuple.append(j)
        else:
          no_int_tuple.append(j)

      print('len_tuple', len_tuple)
      print('no_int_tuple', no_int_tuple)
      # if range(no_int_tuple) != 0:
        #   calculate_structure_sum(*j)
      # print('len_tuple', len_tuple)

# numbers = (10, 20, 30, 40, 50)
# total = sum(numbers)
# print(total)  # Выведет: 150 (сумма всех чисел в кортеже) [1](https://ru.hexlet.io/qna/python/questions/kakaya-funktsiya-nuzhna-dlya-slozheniya-chisle-v-python)


result = calculate_structure_sum(*data_structure)
print(result)

# Выходные данные (консоль):
# 99

# Примечания (рекомендации):
# Весь подсчёт должен выполняться одним вызовом функции.
# Рекомендуется применить рекурсивный вызов функции, для каждой внутренней структуры.
# Т.к. каждая структура может содержать в себе ещё несколько элементов, можно использовать параметр *args
# Для определения типа данного используйте функцию isinstance.
