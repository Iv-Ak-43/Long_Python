# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
import string


# Здесь пишем код
def generate_random_name():
    while True:
        # Первое слово
        first_word_length = random.randint(1, 15)
        first_word = ''.join(random.choices(string.ascii_lowercase, k=first_word_length))

        # Второе слово
        second_word_length = random.randint(1, 15)
        second_word = ''.join(random.choices(string.ascii_lowercase, k=second_word_length))

        yield f"{first_word} {second_word}"


# Пример использования генератора
gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
