# 1차 제출: 풀이 시간 30분? 근데 더럽게 풀었음
# 2차 제출: 행 바뀔때 + 두번 해줘서 수정 (161868kb, 1520ms)
# 3차 제출: 행이랑 열 따로 넣자 (1520ms -> 824ms)
# https://www.acmicpc.net/problem/17136
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def dfs(r, c, result, matrix):
    global answer
    if r >= 10 or c >= 10:
        answer = min(result, answer)
        return
    elif result > answer: return

    if matrix[r][c]:
        for i in range(5,0,-1):
            if not paper[i-1]: continue
            elif r+i > 10 or c+i > 10: continue
            elif all([all(row[c:c+i]) for row in matrix[r:r+i]]):
                paper[i-1] -= 1
                lst = [(x,y) for x in range(r,r+i) for y in range(c,c+i)]
                for x,y in lst:
                    matrix[x][y] = 0

                nr, nc = lst[i-1]
                nr, nc = (nr+1, 0) if nc == 9 else (nr, c+1)

                dfs(nr, nc, result+1, matrix)
                for x,y in lst:
                    matrix[x][y] = 1
                paper[i-1] += 1
    else:
        nr, nc = (r+1, 0) if c == 9 else (r, c+1)
        dfs(nr, nc, result, matrix)

matrix = [list(map(int, input().split())) for _ in range(10)]
paper = [5,5,5,5,5]
answer = 26
dfs(0, 0, 0, matrix)
print(-1 if answer == 26 else answer)