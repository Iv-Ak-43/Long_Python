string_file = input("Введите абсолютный путь до файла: ")
file_name = string_file.split("/")[-1].split("\\")[-1].split(".")[0]
print("Название файла:", file_name)
