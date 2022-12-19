# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

print('Введите число')
num = int(input())

print ('Сумма чисел последовательности (1+1/n)**n будет равна:')
for i in range(1, num+1):
    composition = round((1+1/i)**i, 0) 
    print(composition, end=" ")