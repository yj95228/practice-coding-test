# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AYnI6Ju6FF0DFAUe&probBoxId=AYnNE126270DFARi&type=USER&problemBoxTitle=11_230807%3A+Backtracking_1&problemBoxCnt=11
import sys
sys.stdin = open('input.txt', 'r')

def dfs(arr):
    global answer
    if len(arr) == M and sum([x[1] for x in arr]) == K:
        answer += 1
    for i, x in enumerate(lst):
        if not arr or arr[-1][0] < i:
            dfs(arr+[(i,x)])

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))
    answer = 0
    dfs([])
    print(f'#{tc} {answer}')

# 강사님 풀이
def dfs(n, start, sm):
    global ans
    if n == M:  # 종료조건
        if sm == K:  # 정답처리는 이곳에서..!
            ans += 1
        return

    # 하부함수 호출
    for j in range(start, N):
        dfs(n + 1, j + 1, sm + lst[j])

# global 없이
def dfs(n, start, sm):
    if n == M:  # 종료조건
        if sm == K:  # 정답처리는 이곳에서..!
            return 1
        return 0

    # 하부함수 호출 => 리턴값을 받아서 리턴
    cnt = 0
    for j in range(start, N):
        cnt += dfs(n + 1, j + 1, sm + lst[j])
    return cnt

TC = int(input())
for tc in range(1, TC + 1):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))

    ans = 0
    # n: 선택한 나라수, start, sum
    dfs(0, 0, 0)
    print(f'#{tc} {ans}')