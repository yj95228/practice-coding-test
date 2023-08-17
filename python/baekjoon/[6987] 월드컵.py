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