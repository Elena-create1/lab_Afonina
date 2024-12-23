#Задание 1
def f(n,m):
  if m=='0':
    with open(n, 'r') as file:
      print(file.read())
  else:
    with open(n, 'r') as file:
      for line in file:
        print(line)
m=str(input('введите 0 для чтения всего файла, иначе 1 '))
f('зад1текст.txt', m)

#Задание 2
with open('user_input.txt', 'w') as f:
    a = str(input('введите что-то '))
    f.write(a+'\n')
print(open('user_input.txt').read())
#задание 2.2
with open('user_input.txt', 'a') as f:
    a=str(input('введите что-то '))
    f.write(a+'\n')
print(open('user_input.txt').read())


#задание 3
file_name=input('введите имя файла с txt ')
def f(n,m):
  try:
    with open(n, 'r') as file:
      if m=='0':
        print(file.read())
      else:
        for line in file:
          print(line)
  except FileNotFoundError:
    print('файл не найден')

m=str(input('введите 0 для чтения всего файла, иначе 1: '))
f(file_name, m)
