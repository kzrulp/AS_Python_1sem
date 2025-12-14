а)
n = int(input())

if n < 0:
    raise ValueError("Отрицательное число")

f = 1
for i in range(1, n + 1):
    f *= i

print(f)

б)
n = int(input())

if n <= 0:
    raise ValueError("Число не является положительным")

print("Число является положительным")


в)
n = int(input())

assert n >= 0, "Отрицательное число"

f = 1
for i in range(1, n + 1):
    f *= i

print(f)
