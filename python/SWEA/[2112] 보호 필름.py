# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V1SYKAaUDFAWu
def recur(n, cnt):
    global answer
    if n == D:
        for c in range(W):
            mx, result = 1, 1
            for r in range(1,D):
                if matrix[r-1][c] == matrix[r][c]:
                    result += 1
                    mx = max(mx, result)
                else: result = 1
            if mx < K: return
        answer = min(answer, cnt)
        return
    if cnt > answer: return

    recur(n+1, cnt)
    row = matrix[n]
    matrix[n] = [0]*W
    recur(n+1, cnt+1)
    matrix[n] = [1]*W
    recur(n+1, cnt+1)
    matrix[n] = row

T = int(input())
for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(D)]
    answer = 987654321
    recur(0, 0)
    print(f'#{tc} {answer}')