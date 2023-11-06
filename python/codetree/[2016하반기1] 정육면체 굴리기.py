import sys
input = sys.stdin.readline

N, M, r, c, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
arr = list(map(lambda x: int(x)-1, input().split()))
dt = ((0,1),(0,-1),(-1,0),(1,0)) # 동, 서, 북, 남
dice = [0]*6    # 위(0), 아래(1), 왼(2), 오(3), 앞(4), 뒤(5)
turn = [
    (2, 3, 1, 0, 4, 5),
    (3, 2, 0, 1, 4, 5),
    (4, 5, 2, 3, 1, 0),
    (5, 4, 2, 3, 0, 1)
]
for d in arr:
    dx, dy = dt[d]
    nx, ny = r+dx, c+dy
    if 0 <= nx < N and 0 <= ny < M:
        dice = list(map(lambda x: dice[x], turn[d]))
        # 칸에 쓰여져 있는 수가 0이면,
        if A[nx][ny] == 0:
            # 주사위의 바닥면에 쓰여져있는 수가 칸에 복사됩니다.
            A[nx][ny] = dice[1]
            # 이때 정육면체의 숫자는 변하지 않습니다.
        # 칸에 쓰여져 있는 수가 0이 아니면
        else:
            # 칸에 쓰여져있는 수가 정육면체 바닥면으로 복사되며,
            dice[1] = A[nx][ny]
            # 해당 칸의 수는 0이 됩니다.
            A[nx][ny] = 0
        # 상단 면에 쓰여져 있는 숫자를 출력
        print(dice[0])
        r, c = nx, ny