# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV597vbqAH0DFAVl
T = int(input())
dt = ((-1,0),(1,0),(0,-1),(0,1))
bandae = [1,0,3,2]
for tc in range(1,T+1):
    N, M, K = map(int, input().split())

    obj = dict()
    for _ in range(K):
        r, c, num, d = map(int, input().split())
        obj[(r,c)] = [(num, d-1)]

    for _ in range(M):
        new_obj = dict()
        for r, c in obj:
            for num, d in obj[(r,c)]:
                dx, dy = dt[d]
                nx, ny = r+dx, c+dy
                if nx == 0 or nx == N-1 or ny == 0 or ny == N-1:
                    new_obj[(nx,ny)] = [(num//2, bandae[d])]
                else:
                    if (nx,ny) in new_obj:
                        new_obj[(nx,ny)].append((num, d))
                    else:
                        new_obj[(nx,ny)] = [(num, d)]

        obj = dict()
        for r, c in new_obj:
            if len(new_obj[(r,c)]) >= 2:
                sm = sum([x[0] for x in new_obj[(r,c)]])
                obj[(r,c)] = [(sm, max(new_obj[(r,c)])[1])]
            else:
                obj[(r,c)] = new_obj[(r,c)]

    print(f'#{tc} {sum([x[0] for r, c in obj for x in obj[(r,c)]])}')