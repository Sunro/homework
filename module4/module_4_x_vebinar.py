from array import array
from random import randint
data = [randint(1, 99) for _ in range(1000)]

# 0(N*N) # 0(logon * N) # 0(n!)

# def bubble(array):
#     iter = len(array) - 1
#     for i in range(iter -1):
#         swapped = False
#         for j in range(iter - 1 - i):
#             if array[j] > array[j+1]:
#                 array[j], array[j+1] = array[j],array[j+1]
#                 swapped = True

def bubble(array):
    iter = len(array) - 1
    for i in range(iter):
        for j in range(iter-i)
            if array[i] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
print(data)
print(array)
bubble(data)