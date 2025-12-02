def InvertStr(S, K, N):
    if K > len(S):
        return ""

    start = K - 1

    end = start + N

    if end > len(S):
        end = len(S)

    substring = S[start:end]

    return substring[::-1]


S = "программирование"

print(InvertStr(S, 3, 5))

print(InvertStr(S, 20, 5))

print(InvertStr(S, 12, 10))

print(InvertStr(S, 1, 20))
