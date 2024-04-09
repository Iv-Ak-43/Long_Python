string1 = input("Введите первую строку: ")
string2 = input("Введите вторую строку: ")

sum_string = string1 + " " + string2
new_string1 = string2[:2] + string1[2:]
new_string2 = string1[:2] + string2[2:]

print("Объединенная строка:", sum_string)
print("Строка после обмена символов:", new_string1)
print("Строка после обмена символов:", new_string2)
