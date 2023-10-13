# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRJ8EKe48DFAUo
def solve():
    NN, MM = len(A), len(A[0])
    narr = [[0]*(MM+2)] + [[0] + row[:] + [0] for row in A] + [[0]*(MM+2)]
    nlive = [[0]*(MM+2)] + [[0] + row[:] + [0] for row in live] + [[0]*(MM+2)]
    for r in range(NN):
        for c in range(MM):
            if not A[r][c]: continue
            # 활성화 상태
            elif A[r][c] <= live[r][c]:
                for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                    nx, ny = r+1+dx, c+1+dy
                    if not A[nx-1][ny-1] and (not narr[nx][ny] or (narr[nx][ny] < A[r][c])):
                        narr[nx][ny] = A[r][c]
                nlive[r+1][c+1] += 1
                # 활성화 다 시켰으면 죽이기
                rr, cc = r+1, c+1
                if nlive[rr][cc] - narr[rr][cc] >= narr[rr][cc]:
                    nlive[rr][cc] = -1
            # 죽지 않은 비활성화 상태
            elif live[r][c] >= 0:
                nlive[r+1][c+1] += 1
    if any(narr[-1]) or any(nlive[-1]):
        narr.pop()
        nlive.pop()
    if any(narr[0]) or any(nlive[0]):
        narr.pop(0)
        nlive.pop(0)
    return narr, nlive

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    live = [[0]*M for _ in range(N)]
    for _ in range(K):
        A, live = solve()
    answer = 0
    for r in range(len(A)):
        for c in range(len(A[0])):
            if not A[r][c]: continue
            if live[r][c] == -1: continue
            answer += 1
    print(f'#{tc} {answer}')