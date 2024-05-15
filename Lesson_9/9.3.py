# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
with open("test_file/task_3.txt", 'r', encoding='utf-8') as file:
    summa = 0
    mass = []
    for line in file:
        line = line.replace('\n','')
        if line != '':
            summa += int(line)
        else:
            mass.append(summa)
            summa = 0
    three_most_expensive_purchases = sum(sorted(mass)[-1:-4:-1])

print(summa)

assert three_most_expensive_purchases == 202346