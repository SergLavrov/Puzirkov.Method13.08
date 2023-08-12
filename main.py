#  Написать функцию, которая реализует алгоритмы
# - "Быстрой сортировки".
# - "Пузырьковый метод"
# # Вводятся следующие параметры:
# # - количество значений (с использованием конструкции try-except)
# # - ввод чисел с клавиатуры (в список) (с использованием конструкции try-except)


# - "Пузырьковый метод"

try:
    lenlist = int(input('Enter the length of the list: '))
except ValueError:
    print('Error: you must enter a number!')
    lenlist = int(input('Enter the length of the list: '))

someList = []

for index in range(lenlist):
    try:
        someList.append(int(input(f'Enter the number {index+1}: ')))

    except ValueError:
        print('Error: you must enter a number!')
        someList.append(int(input(f'Enter the number {index+1}: ')))

n = 1
while n < len(someList):
   for i in range(len(someList) - n):
       if someList[i] > someList[i + 1]:
           someList[i], someList[i + 1] = someList[i + 1], someList[i]
   n += 1

print(someList)
