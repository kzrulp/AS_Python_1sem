#Дана строка-предложение. Подсчитайте вхождение каждого слова в данное предложение.
predl = input("Введите предложение: ").lower().split()

word_ct = {}
for word in predl:
    word_ct[word] = word_ct.get(word, 0) + 1

print("Результат:")
for word, count in word_ct.items():
    print(f"'{word}': {count}")

