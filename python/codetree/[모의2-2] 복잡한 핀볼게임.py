from sys import stdin
input = stdin.readline

def play(matrix):
    visited = [[0]*N for _ in range(N)]
    pinball = [row[:] for row in where]
    explode = set()
    for i in range(4*N-1,-1,-1):
        if arr[i]:
            r, c, d = pinball[i]
            if not visited[r][c]:
                visited[r][c] = 1
                nd = turn[matrix[r][c]][d]
                pinball[i] = [r, c, nd]
            else:
                pinball.pop(i)
                explode.add((r,c))
        else: pinball.pop(i)

    for i in range(len(pinball)-1,-1,-1):
        r, c, _ = pinball[i]
        if (r,c) in explode:
            pinball.pop(i)

    result = 0
    while pinball:
        narr = [[0]*N for _ in range(N)]
        explode = set()
        for i in range(len(pinball)-1,-1,-1):
            r, c, d = pinball[i]
            dx, dy = dt[d]
            nx, ny = r+dx, c+dy
            if 0 <= nx < N and 0 <= ny < N:
                if not narr[nx][ny]:
                    narr[nx][ny] = 1
                    nd = turn[matrix[nx][ny]][d]
                    pinball[i] = [nx, ny, nd]
                else:
                    explode.add((nx, ny))
                    pinball.pop(i)
            else:
                result += 1
                pinball.pop(i)

        for i in range(len(pinball)-1,-1,-1):
            r, c, _ = pinball[i]
            if (r,c) in explode:
                pinball.pop(i)
    return result


def recur(n, matrix):
    global answer
    if n == length:
        answer = max(answer, play(matrix))
        return
    narr = [row[:] for row in matrix]
    r, c = blank[n]
    narr[r][c] = 0
    recur(n+1, narr)
    narr[r][c] = 1
    recur(n+1, narr)
    narr[r][c] = 2
    recur(n+1, narr)

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
dt = ((-1,0),(0,1),(1,0),(0,-1))
turn = ((0,1,2,3),(1,0,3,2),(3,2,1,0))
arr = list(map(int, input().split()))
where = [(0,x,2) for x in range(N)] + [(x,N-1,3) for x in range(N)] + [(N-1,N-x-1,0) for x in range(N)] + [(N-x-1,0,1) for x in range(N)]
blank = []
for r in range(N):
    for c in range(N):
        if matrix[r][c] == 3:
            blank.append((r,c))
length = len(blank)
answer = 0
recur(0, matrix)
print(answer)