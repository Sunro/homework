nums = [5, 6, 2, 1, 3, 4]
# см скриншот 241224_0119
def buble_sort(ls):
    # чтобы цикл сработал хотя бы один раз, задаём значение True
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i + 1]:
                # меняем элементы местами
                ls[i], ls[i + 1] = ls[i+1], ls[i]
                # меняем значение переменной swap для следующего повтора цикла
                swapped = True

buble_sort(nums)
print(nums)

def selection_sort(ls):
    # i - кличество отсортированных элементов
    for i in range(len(ls)):
        # изначально считаем минимальным первый элемент
        lowest = i
        цикл для перебора неотсортированных элементов
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[lowest]: #Tab to complete
                lowest = j
            самый минимальный элемент меняем с первым элементом
            ls[i], ls[lowest] = ls[lowest], ls[i]

selection_sort(nums)
print(nums)



