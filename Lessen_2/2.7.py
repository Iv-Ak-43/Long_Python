first_string = input("Введите строку: ")
second_string = input("Введите строку: ")

slice_start = second_string.find(first_string[0])
slice_end = second_string.rfind(first_string[-1]) + 1

result_slice = second_string[slice_start:slice_end]
print("Срез минимальной длины:", result_slice)
