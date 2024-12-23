#задание 1

def greet(name):
    print('Здравствуйте,', name,'!')
    
def square(n):
    return n**2

def max_of_two(a,b):
    return max(a,b)

function_choice = input('Введите название функции, которую хотите запустить (greet,square,max_of_two): ')
if function_choice == 'greet':
    name = input('Ваше имя: ')
    greet(name)
elif function_choice == 'square':
    n = int(input('Введите число, квадрат которого необходимо найти: '))
    print('Квадрат числа = ',square(n))
elif function_choice == 'max_of_two':
    a = int(input('Введите 1 число: '))
    b = int(input('Введите 2 число: '))
    print('Максимальное из данных чисел =', max_of_two(a,b))
else:
    print('Функция не найдена!')



#задание 2

def describe_person(name,age):
    if age == 'нет':
        age = 30
    print('Имя:',name,'\nВозраст:',age)
    
name = input('Введите имя: ')
age = input("Введите возраст(опционально). При отказе введите 'нет': ")
describe_person(name,age)



#задание 3

def is_prime(number):
    if number < 2:
        return False
    else:
        k = 0
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                k = k + 1
                return False
    return True

number = int(input('Введите число '))
print(is_prime(number))
