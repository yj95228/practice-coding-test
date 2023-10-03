'''
- 1차. Value Error
- 2차. 미친 아두이노가 옮길 자리에 위치 옮기기 전의 아두이노가 이미 있으면 폭발 X
'''
# https://www.acmicpc.net/problem/8972
from sys import stdin
stdin = open('python/baekjoon/input.txt','r')
input = stdin.readline

def play(sr,sc,queue,matrix):
    for time, d in enumerate(arr, start=1):
        
        new_matrix = [['.']*C for _ in range(R)]

        # 종수 이동
        dx, dy = dt[d]
        nx, ny = sr+dx, sc+dy

        if matrix[nx][ny] == 'R':
            return f'kraj {time}'
        else:
            new_matrix[nx][ny] = 'I'
            sr, sc = nx, ny

        # 로봇 이동
        robot, explode = [], set()
        for r, c in queue:
            mn = 987654321
            rr, cc = None, None
            
            # 방향 결정
            for dx, dy in dt:
                nx, ny = r+dx, c+dy
                sm = abs(nx-sr)+abs(ny-sc)
                if sm < mn:
                    mn = sm
                    rr, cc = nx, ny
                    
            if new_matrix[rr][cc] == 'I':
                return f'kraj {time}'
            elif new_matrix[rr][cc] == 'R':
                explode.add((rr,cc))
            else:
                new_matrix[rr][cc] = 'R'
                robot.append((rr,cc))

        for r, c in explode:
            robot.remove((r,c))
            new_matrix[r][c] = '.'

        queue = [e[:] for e in robot]
        matrix = new_matrix

    else:
        return '\n'.join([''.join(row) for row in matrix])
            

R, C = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(R)]
dt = ((1,-1),(1,0),(1,1),(0,-1),(0,0),(0,1),(-1,-1),(-1,0),(-1,1))
arr = list(map(lambda x: int(x)-1, list(input().rstrip())))

sr, sc = None, None
queue = []
for r in range(R):
    for c in range(C):
        if matrix[r][c] == 'I':
            sr, sc = r, c
        elif matrix[r][c] == 'R':
            queue.append((r, c))

print(play(sr,sc,queue,matrix))