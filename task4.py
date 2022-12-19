# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в отдельном списке
# ( пример n=4, lst1=[4,-2,1,3] - списко на основе n, а позиции элементов lst2=[3,1].


import random
print('Введите число')
num = int(input())
print()

numbers = list()
i = 0
while num > i:
    rat = random.randint(-num, num)
    numbers.append(rat)
    i = i+1
print('Список из N элементов:', numbers)

position = [random.randint(0, num-1), random.randint(0, num-1)]
print('Рандомные поцизии элементов ', position)

result = numbers[position[0]]*numbers[position[1]]
print('Произведение элементов на позициях [', position[0], '] и [', position[1], '] равна ', result)
