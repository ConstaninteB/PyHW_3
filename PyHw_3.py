# ; Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# ; Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# ; В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# ; n = 5
# ; 1 2 3 4 5
# ; x = 3

# ; -> 1

from random import randint
length = int(input("Введите длинну списка: "))
random_list = []
for i in range(length):
     random_list.append(randint(0, 10))
print(random_list)     
Find_num = int(input("Введите число от 1 - 9, кторое нужно найти в списке: "))
cnt = 0
for i in random_list:
    if i == Find_num:
     cnt += 1 
print(cnt)    