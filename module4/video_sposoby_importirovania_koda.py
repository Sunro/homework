# 4_2_video_sposoby_importirovania_koda

from random import randint
from dis import dis
# from module1 import module_1_7

# print(students_middle_grades)
def say_hi():
    print('Привет я из функции в подключенном модуле')
    from random import randint
    print(randint(1, 10))

dis(say_hi)

# randint() глобально не импортирован и не запуститcя, будет ошибка

from module1.module_1_7 import * # "*" - не работает внутри функции
def main():
    a = 5
    b = 10
    print('Привет')
    import module1.module_1_7 as md1_7
    print(students_middle_grades_round)
    print(md1_7.students_middle_grades_round)


if __name__ == '__main__':
    main()