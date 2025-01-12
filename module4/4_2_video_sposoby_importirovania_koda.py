# Все видео и вебинар 4го модуля
from video_sposoby_importirovania_koda import say_hi as sh
print('Я из главного модуля')
import sys
import math
import random
import tkinter
import simple_draw
import module4.simple_draw
import unsort.vebinar
# чтоб избежать циклического импорта не нужно в обоих модулях импортировать друг друга
# нужно создать 3й модуль и выбрать необходимое из предыдущих 2х модулей
sh()
b = 10
for path in sys.path:
    print(path)

print(dir(math))
print(dir(list))

# Очень большая часть анализа данных в python и bigdata она построена на питоне, в питоне есть крутые библиотеки
# NumPy and Pandas c этим тоже можно учиться работать

# Если написать команду ls можно узнать список файлов и папок
# source urban/bin/activate
# deactivate
# снимок экрана 241223_0035 - консоль линукс в виндовс нужно самим разобраться
# чтоб всё стабильно работало для каждого проэкта нужно своё виртуальное окружение
# для создания файла в терминале можно прописать аналог линуксового touch для powershell
# python 4_2_video_sposoby_importirovania_koda.py - запускает код файла