f = open('text.txt', 'r')
lines = f.readlines()
f.close()

f = open('text.txt', 'w')

for l in lines:
    l = line[:-1]   

    if l != '':
        if len(l) % 2 == 1:
            l = ' ' + l

        k = (50 - len(l)) // 2
        f.write(' ' * k + l)

    f.write('\n')

f.close()
