# задание 1.1
import math
def f(n):
    if n<0: print('корень не вычисляется')
    else: print('квадрат числа: ', math.sqrt(n))
a=int(input('ввeдите число: '))
f(a)

# задание 1.2
import datetime
print(datetime.datetime.now())

# задание 2
import my_module
a=int(input('введите число: '))
b=int(input('введите число: '))
print(my_module.summ(a,b))

# задание 3
from jkbjdfh import module1, module2

#фунция сложения
a=int(input('введите число: '))
b=int(input('введите число: '))
print(module1.summ(a,b))

#функция приветсвия
z=input('введите имя ')
module2.prvt(z)
