#Для заданного натурального n и действительного x подсчитать сумму:\begin{align} \sin{x} + \sin{x^2} + \sin{x^3} + ... + \sin{x^n}. \end{align}

код:
import math

n = int(input("n: "))
x = float(input("x: "))

t = sum(math.sin(x ** k) for k in range(1, n + 1))
print(f"Сумма = {t}")
