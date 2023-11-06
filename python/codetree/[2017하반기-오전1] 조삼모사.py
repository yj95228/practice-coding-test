def recur(n, a, b, asum, bsum, arr, brr):
    global answer
    if a > b and a-b > N-n: return
    elif b > a and b-a > N-n: return
    if n == N:
        if a == b:
            answer = min(answer, abs(asum-bsum))
        return

    asm = asum
    for x in arr:
        asm += A[x][n] + A[n][x]
    recur(n+1, a+1, b, asm, bsum, arr+[n], brr)
    bsm = bsum
    for y in brr:
        bsm += A[y][n] + A[n][y]
    recur(n+1, a, b+1, asum, bsm, arr, brr+[n])

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
answer = 987654321
recur(0, 0, 0, 0, 0, [], [])
print(answer)