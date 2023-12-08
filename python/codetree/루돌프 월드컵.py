def recur(n, p, s):
    if n == 6:
        if (s[0] >= s[1]) + (s[0] >= s[2]) + (s[0] >= s[3]) >= 2:
            global answer
            answer += p
        return

    r1, r2 = sequence[n]
    f1, f2 = arr[r1], arr[r2]

    pp, ss = p, s[:]
    pp *= 4 * f1 / (5 * f1 + 5 * f2)
    ss[r1] += 3
    recur(n + 1, pp, ss)

    pp, ss = p, s[:]
    pp *= 4 * f2 / (5 * f1 + 5 * f2)
    ss[r2] += 3
    recur(n + 1, pp, ss)

    pp, ss = p, s[:]
    pp *= (f1 + f2) / (5 * f1 + 5 * f2)
    ss[r1] += 1
    ss[r2] += 1
    recur(n + 1, pp, ss)


arr = list(map(int, input().split()))
sequence = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
answer = 0
recur(0, 1, [0] * 4)
print(f'{answer * 100:.3f}')