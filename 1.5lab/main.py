# Дан список. Выбрать из списка все числа меньше 15 и упорядочить их по убыванию.
num = list(map(int, input("Введите список: ").split()))
men15 = []
for x in num:
    if x < 15:
        men15.append(x)
men15.sort(reverse=True)

print(men15)
