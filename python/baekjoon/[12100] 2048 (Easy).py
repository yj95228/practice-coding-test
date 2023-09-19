# 1차 제출: 10:15 대충 다 짜고 배열 잘 돌아가는지 확인해보고 10:27 제출
# 2차 제출: (10:35) 0은 왼쪽으로 보내고 멀리 떨어진 숫자도 합쳤어야 함 (116084kb, 228ms)
# 3차 제출: deque로 풀면 속도 얼마 걸리는지 확인 (228ms -> 276ms)
# 4차 제출: recur() 넣을 때 어차피 play2048()에서 처리하니까 복사 안하고 그냥 넣어도 됨 (228ms -> 240ms)
# https://www.acmicpc.net/problem/12100
import sys
input = sys.stdin.readline

def play2048(matrix):
    new_matrix = []
    for row in matrix:
        new_row = []
        queue = list(row[:])
        while queue:
            x = queue.pop(0)
            if x == 0: continue
            while queue and queue[0] == 0:
                queue.pop(0)
            if queue and x == queue[0]:
                queue.pop(0)
                new_row.append(x*2)
            else:
                new_row.append(x)
        new_row.extend([0]*(N-len(new_row)))
        new_matrix.append(new_row)
    return new_matrix

def recur(n, matrix):
    global answer
    answer = max(max([x for row in matrix for x in row]), answer)
    if n == 5:
        return

    # 현재 방향 그대로
    recur(n+1, play2048(matrix))
    # 시계 방향 돌려서 넣기
    recur(n+1, play2048(list(zip(*matrix[::-1]))))
    # 180도 돌려서 넣기
    recur(n+1, play2048([row[::-1] for row in matrix[::-1]]))
    # 반시계 방향 돌려서 넣기
    recur(n+1, play2048(list(zip(*matrix))[::-1]))

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
answer = 0
recur(0, matrix)
print(answer)