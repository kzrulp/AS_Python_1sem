f = open('input.txt', 'r')

k = int(f.readline())

f1 = open('sym.txt', 'w')
f2 = open('other.txt', 'w')

for t in range(k):
    n = int(f.readline())
    a = []

    for i in range(n):
        a.append(f.readline().split())

    ok = True

    for i in range(n):
        for j in range(n):
            if a[i][j] != a[j][i]:
                ok = False

    if ok:
        f1.write(str(n) + '\n')
        for i in range(n):
            f1.write(' '.join(a[i]) + '\n')
    else:
        f2.write(str(n) + '\n')
        for i in range(n):
            f2.write(' '.join(a[i]) + '\n')

f.close()
f1.close()
f2.close()
