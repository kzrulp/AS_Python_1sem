def Simm(S):
    if len(S) <= 1:
        return True

    if S[0] != S[-1]:
        return False

    return Simm(S[1:-1])


проверка:
text = input("Введите строку: ")

if Simm(text):
    print("Строка симметрична")
else:
    print("Строка не симметрична")
