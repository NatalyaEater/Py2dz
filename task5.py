# Реализуйте алгоритм перемешивания списка. (рандомно поменять местами элементы списка между собой)

import random

print('Введите кол-во позиций для списка')
num = int(input())
print('')

numbers = list()
k = 0
while num > k:
    rat = random.randint(-10, 10)
    numbers.append(rat)
    k = k+1
print('Первоначальный вид списка', numbers)

i = 0
while num > i:
    j = random.randint(0, num-2)
    step = numbers[i]
    numbers[i] = numbers[j]
    numbers[j] = step
    i = i+1
print('Перемешанный  вид списка', numbers)
