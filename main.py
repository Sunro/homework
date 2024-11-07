# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hello {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('world')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print("Hello world")
print(f'{__name__}')


#типы данных
print(5+5)
print(5-5)
print(5*5)
print(5/5)
print(5//5)
print(5%5)
print(5**5)
print(type(2.0))
#print(Hello, world)
print('Hello, world')
print(type('Hello, world'))
print (5!=5 and 5<10)
print (5==5 and 5<10)
print(type(int('5')))

#1st program
print(9**0.5*5)
#2nd program
print(9.99>0.98 and 1000!=1000.1)
#3rd program
print(2*2+2)
print(2*(2+2))
print(2*2+2==2*(2+2))
#4th program
print(int((float(123.456)*10)%10))

#Практическая работа по уроку динамическая типизация
name='Vladimir'
print('Name:',name)
age=36
print('Age:',age)
age='24'
print('New age:', age)
is_student=True
print('Is Student:', is_student)
print(is_student, type(is_student))

