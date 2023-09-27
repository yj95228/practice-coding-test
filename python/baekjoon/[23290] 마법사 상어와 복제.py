'''
- 둘다 구현 문제인데 상어 디버깅 빡셀 것 같아서 어항정리 먼저 풀어보자 -> 13:10
- 30분에서 한시간 풀어보고 힘들면 상어로 넘어가야지
- 한시간 어항 바닥에 놓는거까지 하고 상어 풀러옴
- 15:35 다 풀었는데 TC6번 틀리고 S 큰거 오래 걸려서 시간초과 날 거 같음
- 상어가 물고기를 못 잡으면 그래도 상상상으로 가야되는데 상어 위치 안 바꿔줌
- 시간초과 날 거 같은데 어떻게 잡지
- 16:36 시간초과 날거 같지만 일단 제출로 저장해놓고 수정하자
- 16:44 코드가 더러워도 일단 제출 ㄱㄱㄱㄱㄱㄱㄱ
- matrix = new_matrix 안 넣어서 변경이 제대로 안 됐음
- filter를 쓰면 많이 느린 것 같다
- 두 번 전 냄새이므로 3으로 해줘야함
'''
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

M, S = map(int, input().split())
matrix = [[[] for _ in range(4)] for _ in range(4)]
dt = ((0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1))
dts = ['←', '↖', '↑', '↗', '→', '↘', '↓', '↙']
for _ in range(M):
    X, Y, D = map(lambda x: int(x)-1, input().split())
    matrix[X][Y].append(D)
sx, sy = map(lambda x: int(x)-1, input().split())
smell = [[0]*4 for _ in range(4)]

for _ in range(S):
    # 1. 복제 마법
    magic = [[row[:] for row in arr2d] for arr2d in matrix]
    new_matrix = [[[] for _ in range(4)] for _ in range(4)]

    # 2. 물고기 이동
    for r in range(4):
        for c in range(4):
            for fish in range(len(matrix[r][c])-1,-1,-1):
                d = matrix[r][c][fish]
                for i in range(8):
                    dx, dy = dt[(d-i)%8]
                    nx, ny = r+dx, c+dy
                    if 0 <= nx < 4 and 0 <= ny < 4 and (nx,ny) != (sx,sy) and not smell[nx][ny]:
                        new_matrix[nx][ny].append((d-i)%8)
                        break
                else:
                    new_matrix[r][c].append(d)

    matrix = new_matrix

    def recur(x,y,n,result,new_matrix,smells):
        global answer, matrix, sx, sy, flag, smell

        matrix2 = [[row[:] for row in arr2d] for arr2d in new_matrix]
        smell2 = [row[:] for row in smells]

        if n >= 3:
            if result > answer or not flag:
                flag = True
                answer = result
                matrix = new_matrix
                smell = smell2
                sx, sy = x, y
            return matrix

        for dx, dy in ((-1,0),(0,-1),(1,0),(0,1)):
            nx, ny = x+dx, y+dy
            if 0 <= nx < 4 and 0 <= ny < 4:
                arr = matrix2[nx][ny]
                tmp = smells[nx][ny]
                if arr:
                    smells[nx][ny] = 3
                    matrix2[nx][ny] = []
                recur(nx,ny,n+1,result+len(arr),[[row[:] for row in arr2d] for arr2d in matrix2],[row[:] for row in smells])
                matrix2[nx][ny] = new_matrix[nx][ny]
                smells[nx][ny] = tmp

    # 3. 상어 이동
    answer = 0
    flag = False
    recur(sx,sy,0,0,new_matrix,smell)

    for r in range(4):
        for c in range(4):
            if smell[r][c]:
                smell[r][c] -= 1
            matrix[r][c].extend(list(filter(lambda x: x >= 0, magic[r][c])))

answer = 0
for arr in matrix:
    for fishes in arr:
        for fish in fishes:
            if fish >= 0:
                answer += 1
print(answer)