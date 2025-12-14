f = open('f.txt', 'r')

num = f.readlines()
f.close()

max_abs = 0
i = 1   

for l in num:
    x = float(l)

    if i % 2 == 1:   
        if abs(x) > max_abs:
            max_abs = abs(x)

    i = i + 1

print(max_abs)
