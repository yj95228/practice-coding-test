'''
- 1차 제출: 0인 그룹들 미리 계산해주고 0 갯수 미리 세놓은 걸 matrix에 적어놓기 -> 시간초과
- 2차 제출: matrix에는 그룹명만 적어놓고 그룹의 cnt는 룩업테이블로 따로
- 3차 제출: DFS -> BFS
- 4차 제출: 더해줄때 visited 말고 set으로
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().rstrip())) for _ in range(N)]
empty = [[0]*M for _ in range(N)]
answer = [[0]*M for _ in range(N)]

cnts = [0]
group = 1
for r in range(N):
    for c in range(M):
        if not matrix[r][c] and not empty[r][c]:
            cnt = 1
            empty[r][c] = group
            stack = [(r,c)]

            while stack:
                x, y = stack.pop()
                for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < N and 0 <= ny < M and not empty[nx][ny] and not matrix[nx][ny]:
                        cnt += 1
                        empty[nx][ny] = group
                        stack.append((nx,ny))
            group += 1
            cnts.append(cnt)

for r in range(N):
    for c in range(M):
        if matrix[r][c] == 1:
            s = set()
            answer[r][c] += 1
            for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                nx, ny = r+dx, c+dy
                if 0 <= nx < N and 0 <= ny < M and not matrix[nx][ny]:
                    s.add(empty[nx][ny])
            for g in s:
                answer[r][c] += cnts[g]
            answer[r][c] %= 10

for row in answer:
    print(''.join(map(str,row)))