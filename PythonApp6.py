word = input("Введите слово, состоящее из маленьких латинских букв: ")

# Счетчик гласных
vowels = 0
# Счетчик согласных
consonants = 0

for char in word:
    # проверка наличия элемента (гласной) в последовательности
    if char in "aeiou":
        vowels += 1
    # проверка наличия элемента (согласной) в последовательности
    elif char in "bcdfghjklmnpqrstvwxyz":
        consonants += 1
    # если нет ни той, ни другой, то false
    else:
        print(False)

print("Количество гласных букв:", vowels)
print("Количество согласных букв:", consonants)