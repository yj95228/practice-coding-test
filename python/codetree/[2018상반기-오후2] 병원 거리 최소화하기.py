def recur(n, start, arr):
    global answer
    if n == M:
        result = 0
        for i in range(len(people)):
            result += min([D[i][x] for x in arr])
        answer = min(answer, result)
        return
    for x in range(start, len(hospital)):
        recur(n+1, x+1, arr+[x])

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
people, hospital = [], []
for r in range(N):
    for c in range(N):
        if A[r][c] == 1:
            people.append((r, c))
        elif A[r][c] == 2:
            hospital.append((r, c))

D = [[0]*len(hospital) for _ in range(len(people))]
for i, (r1, c1) in enumerate(people):
    for j, (r2, c2) in enumerate(hospital):
        D[i][j] = abs(r1-r2)+abs(c1-c2)

answer = 987654321
recur(0, 0, [])
print(answer)