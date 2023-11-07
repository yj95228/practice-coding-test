N, L = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
answer = 0

for r in range(N):
    V = [0]*N
    now = 1
    flag = False
    while now < N:
        if flag: break
        elif abs(A[r][now-1] - A[r][now]) > 1:
            flag = True
            break
        elif A[r][now] == A[r][now-1]: now += 1
        elif A[r][now]-A[r][now-1] == 1:    # 2 2 3
            for i in range(1, L+1):
                if now-i < 0 or V[now-i]:
                    flag = True
                    break
                elif A[r][now]-A[r][now-i] == 1:
                    continue
                else:
                    flag = True
                    break
            else:
                for i in range(1, L+1):
                    V[now-i] = 1
                now += 1
        elif A[r][now-1]-A[r][now] == 1:    # 3 2 2
            for i in range(L):
                if now+i >= N or V[now+i]:
                    flag = True
                    break
                elif A[r][now-1]-A[r][now+i] == 1:
                    continue
                else:
                    flag = True
                    break
            else:
                for i in range(L):
                    V[now+i] = 1
            now += L
    if not flag: answer += 1

for c in range(N):
    V = [0]*N
    now = 1
    flag = False
    while now < N:
        if flag: break
        elif abs(A[now-1][c] - A[now][c]) > 1:
            flag = True
            break
        elif A[now][c] == A[now-1][c]: now += 1
        elif A[now][c]-A[now-1][c] == 1:    # 2 2 3
            for i in range(1, L+1):
                if now-i < 0 or V[now-i]:
                    flag = True
                    break
                elif A[now][c]-A[now-i][c] == 1:
                    continue
                else:
                    flag = True
                    break
            else:
                for i in range(1, L+1):
                    V[now-i] = 1
                now += 1
        elif A[now-1][c]-A[now][c] == 1:    # 3 2 2
            for i in range(L):
                if now+i >= N or V[now+i]:
                    flag = True
                elif A[now-1][c]-A[now+i][c] == 1:
                    continue
                    break
                else:
                    flag = True
                    break
            else:
                for i in range(L):
                    V[now+i] = 1
            now += L
    if not flag: answer += 1

print(answer)