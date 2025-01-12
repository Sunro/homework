from dop_to_module4.practice_1_2 import *
data_1 = list(map(int, input('Введите числа через пробел: ').split()))
data_2 = list(map(int, input('Введите числа через пробел: ').split()))
data_3 = list(map(int, input('Введите числа через пробел: ').split()))
print(data_1)

bubble_sort(data_1)
selection_sort(data_2)
insertion_sort(data_3)

print('Пузырьковая сортировка:', data_1)
print('Сортировка выбором:', data_2)
print('Сортировка вставкой:', data_3)