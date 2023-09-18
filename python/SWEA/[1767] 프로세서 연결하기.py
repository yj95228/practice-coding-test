# 1차 제출: 소요시간 20분 정도
# 2차 제출: 최대한 많은 core에 전원을 연결하였을 경우라는 조건을 빼먹음
# 3차 제출: 연결이 안 될 경우에 대해 재귀를 돌리지 않음
# 4차 제출: for문 다 돌고나서 재귀 돌렸어야 했는데 for 돌면서 연결 안 될 때마다 재귀 돌림
# 5차 제출: 이미 연결된 거는 리스트에 넣지 않기
# 6차 제출: min값을 987654321로 초기화했었는데 해당 값도 같이 answer로 갱신해버림 (85,176kb, 1,659ms)
# 7차 제출: 나머지 다 연결해도 최대값을 갱신할 수 없는 경우 가지치기 (65,792 kb, 383 ms)
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4suNtaXFEDFAUf
import sys
sys.stdin = open('input.txt', 'r')

def recur(n, cnt, matrix, result):
    global mx, answers
    mx = max(cnt, mx)
    answers[cnt] = min(result, answers[cnt])
    if cnt+(len(core)-n) < mx:
        return
    if n == len(core):
        return

    r, c = core[n]
    for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
        i = 1
        new_matrix = [row[:] for row in matrix]
        nx, ny = r+i*dx, c+i*dy
        while (0 <= nx < N and 0 <= ny < N) and not new_matrix[nx][ny]:
            new_matrix[nx][ny] = 1
            i += 1
            nx, ny = r+i*dx, c+i*dy

        if not (0 <= nx < N and 0 <= ny < N):
            recur(n+1, cnt+1, new_matrix, result+i-1)
    recur(n+1, cnt, matrix, result)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    core = []
    for r in range(1,N-1):
        for c in range(1,N-1):
            if matrix[r][c]:
                core.append((r,c))

    mx, answers = 0, [987654321]*(len(core)+1)
    recur(0, 0, matrix, 0)
    answer = 0
    for x in answers:
        if 0 < x < 987654321: answer = x
    print(f'#{tc} {answer}')