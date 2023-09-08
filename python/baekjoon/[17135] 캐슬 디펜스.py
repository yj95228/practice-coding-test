# FIXME: [1] 공격 대상 찾을 때 정렬하는 대신 최소값만 찾도록 코드 수정 (1460ms -> 316ms)
# [2] 아래 줄 없앨 때 filter 대신 직접 for문으로 순회해서 시간 줄어드는지 확인용 제출 (316ms -> 220ms)
# [3] 37번 라인 적 있을 때만 new_enemy ? enemies = new_enemy : break (220ms -> 212ms)
# [4] 재귀로 조합 대신 3중 for문으로 변경 (212ms -> 268ms)
# https://www.acmicpc.net/problem/17135

import sys
input = sys.stdin.readline

def dfs(n,start,arr):
    global answer
    if n == 3:
        result = 0
        # 3명의 궁수 조합마다 적들에게 공격하기 위해 enemy 배열 복사
        enemies = [e[:] for e in enemy]
        castle = N
        while castle:
            # 공격 가능 대상 찾기
            attack = set()
            for i in arr:
                distance, row, column = 100, 0, M+1
                for r, c in enemies:
                    d = castle-r+abs(i-c)
                    if d <= D:
                        if d < distance:
                            distance, row, column = d, r, c
                        elif d == distance and c < column:
                            row, column = r, c
                if column != M+1: attack.add((row,column))
            # 공격하기
            for r,c in attack:
                enemies.remove((r,c))
                result += 1
            castle -= 1
            # 공격 못하면 가장 아래줄에 있던 적들 사라짐
            new_enemy = []
            for r, c in enemies:
                if r < castle:
                    new_enemy.append((r,c))
            if new_enemy:
                enemies = new_enemy
            else: break
        answer = max(result, answer)
        return
    for i in range(start,M):
        dfs(n+1, i+1, arr+[i])

N, M, D = map(int, input().split())
matrix = [input().split() for _ in range(N)]
enemy = []    # 적들 위치 담을 배열
for r in range(N):
    for c in range(M):
        if matrix[r][c] == '1':
            enemy.append((r,c))
answer = 0
dfs(0,0,[])
print(answer)