# TODO: 풀었지만 얻어걸린 느낌..?
# https://www.acmicpc.net/problem/6987
import sys
input = sys.stdin.readline

def dfs(i,j,cnt):
    global result
    if result: return
    if cnt >= 15 or (i >= 5 and j >= 6):
        s = set(sum(arr,[]))
        if len(s) == 1 and 0 in s:
            result = 1
            return
    for k in range(3):
        if arr[i][k] and arr[j][2-k]:
            arr[i][k] -= 1
            arr[j][2-k] -= 1
            if j == 5: dfs(i+1,i+2,cnt+1)
            else: dfs(i,j+1,cnt+1)
            arr[i][k] += 1
            arr[j][2-k] += 1

answer = []
for _ in range(4):
    arr = list(map(int, input().split()))
    if 6 in arr: answer.append(0)
    else:
        arr = [arr[3*i:3*(i+1)] for i in range(6)]
        result = 0
        dfs(0,1,0)
        answer.append(result)
print(*answer)

# 강사님 코드
def solve(result):
    g_cnt = [sum(rs) for rs in result].count(5) # 승무패의 합이 5인 나리의 수
    if g_cnt != 6: return 0    # 승무패의 합이 5인 나라의 수가 6이 아니면 기자 결과 문제있으므로 다음 결과로
    return play(0, result)

def play(no, result):
    if no == 15: return 1
    team1, team2 = games[no]
    for r1 in range(3):
        r2 = 2-r1
        if result[team1][r1] > 0 and result[team2][r2] > 0:
            result[team1][r1] -= 1
            result[team1][r1] -= 1
            if play(no+1, result): return 1
            result[team1][r1] += 1
            result[team2][r2] += 1
    return 0

def make_games():
    for a in range(6):
        for b in range(a+1,6):
            games.append((a,b))
games = []
make_games()
for _ in range(4):
    info = list(map(int, input().split()))
    result = [info[s:s+3] for s in range(0,6,3)]
    print(solve(result), end=' ')