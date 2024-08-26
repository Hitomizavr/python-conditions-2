word = input("Введите слово, состоящее из маленьких латинских букв: ");

vowels = "aeiou";
consonants = "bcdfghjklmnpqrstvwxyz";

# Счетчик гласных
vowelsCount = 0;

# Счетчик согласных
consonantsCount = 0;

for char in word:
    # проверка наличия элемента (гласной) в последовательности
    if char in vowels:
        vowelsCount += 1;

    # проверка наличия элемента (согласной) в последовательности
    elif char in consonants:
        consonantsCount += 1;

print("Количество гласных букв:", vowelsCount);
print("Количество согласных букв:", consonantsCount);


print("\nДетализация гласных букв:");

# Подсчитываем количество каждой гласной в слове отдельно
for letter in vowels:
    count = word.count(letter);

    if count > 0:
        print(letter, "-", count);
    else:
        print(letter, "- False");
