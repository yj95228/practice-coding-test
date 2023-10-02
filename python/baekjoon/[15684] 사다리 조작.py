# https://www.acmicpc.net/problem/15684
# 1차 제출: 문제 읽기 10분 -> 풀기 9:55 시작 -> 10:47 완료 (62분 소요)
# 2차 제출: 가지치기 조건을 or로 했어야 했는데 실수로 and로 적음
# 코드 수정하고 바로 제출할 뻔함
# (테스트 케이스 돌려서 잘 작동되는지 확인해봐야 하는데 맨날 성질 급해서 테스트 안 해보고 코드 고치고 나서 바로 제출하려고 함)
# 3차 제출: i번 가로선의 결과가 i번이 나오면 재귀를 안 돌아도 되게 바꿔봄
# 4차 제출: 사다리 그릴 때 주변에 선 못 그리게 막으면서 재귀 타기 (구현이 어려워서 3차 제출 이후 20분 소요)
# 5차 제출: 이미 찾은 최솟값보다 추가해야되는 선 수가 많으면 가지치기 + 변수명 변경
# 6차 제출: 시간 얼마 안남아서 일단 제출
# 7차 제출: 세로선 그리고 나서 주변에 못 그릴때 +-2 해줬어야 했는데 +-1 함
# 8차 제출: 주변에 선 그어져 있으면 재귀 못 돌게
# 9차 제출: 질문 게시판 참고해서 한쪽만 체크하도록 변경
# 10차 제출: 갈아엎고 새로 짬
# 11차 제출: cnt > 3 -> cnt >= 3로 수정 (118080kb, 5824ms)
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def play():
    for i in range(1,N+1):
        now = i
        for r in range(H):
            if matrix[r][now]:
                now += 1
            elif matrix[r][now-1]:
                now -= 1
        if now != i:
            return False
    return True

def recur(n, cnt):
    global answer
    if cnt >= 3 or cnt > answer or n > len(lines):
        return

    for i in range(n, len(lines)):
        r, c = lines[i]
        if not (matrix[r][c-1] or matrix[r][c] or matrix[r][c+1]):
            matrix[r][c] = 1
            if play(): answer = min(cnt+1, answer)
            else: recur(n+1, cnt+1)
            matrix[r][c] = 0

N, M, H = map(int, input().split())
matrix = [[0]*(N+1) for _ in range(H)]
for _ in range(M):
    A, B = map(int, input().split())
    matrix[A-1][B] = 1

lines = []
for r in range(H):
    for c in range(1,N):
        if not (matrix[r][c-1] or matrix[r][c] or matrix[r][c+1]):
            lines.append((r,c))

if play():
    print(0)
else:
    answer = 4
    recur(0, 0)
    print(-1 if answer == 4 else answer)


# 두번째 풀이
def play():
    for c in range(N):
        now = c
        for r in range(H):
            if now < N-1 and matrix[r][now] == 1:
                now += 1
            elif 0 <= now-1 and matrix[r][now-1] == 1:
                now -= 1
        if c != now: return False
    return True

def recur(n, start, cnt):
    global answer

    if n > 3 or cnt >= answer: return

    if play():
        answer = min(answer, cnt)
        return
    else:
        for i in range(start, len(can_place)):
            r, c = can_place[i]
            if 0 <= c-1 and matrix[r][c-1] == 1: continue
            matrix[r][c] = 1
            recur(n+1, i+1, cnt+1)
            matrix[r][c] = 0

N, M, H = map(int, input().split())
matrix = [[0]*(N-1) for _ in range(H)]
can_place = [(r,c) for r in range(H) for c in range(N-1)]

for _ in range(M):
    a, b = map(lambda x: int(x)-1, input().split())
    matrix[a][b] = 1
    can_place.remove((a,b))
    if 0 <= b-1 and (a,b-1) in can_place: can_place.remove((a,b-1))
    if b+1 < N-1 and (a,b+1) in can_place: can_place.remove((a,b+1))

answer = 4
recur(0,0,0)
print(-1 if answer == 4 else answer)