# FIXME: 원아웃일때도 1루,2루,3루를 아웃시켰음
# https://www.acmicpc.net/problem/17281
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def perm(n, arr):
    global answer
    if n == 3:
        perm(n+1, arr+[0])
    elif n == 9:
        result, idx = 0, 0
        for inning in range(N):
            out = 0
            first, second, third = 0, 0, 0
            while out < 3:
                score = matrix[inning][arr[idx]]
                if score == 0:
                    out += 1
                elif score == 1:
                    result += third
                    first, second, third = 1, first, second
                elif score == 2:
                    result += second+third
                    first, second, third = 0, 1, first
                elif score == 3:
                    result += first+second+third
                    first, second, third = 0, 0, 1
                else:
                    result += first+second+third+1
                    first, second, third = 0, 0, 0
                idx = (idx+1)%9
        answer = max(answer, result)
        return
    else:
        for x in range(1,9):
            if not visited[x]:
                visited[x] = True
                perm(n+1, arr+[x])
                visited[x] = False

# 1264ms -> 1044ms
# FIXME: for inning in matrix으로 바로 바라보게 하고 insert(3,0)으로 재귀 깊이 줄이기
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [False]*9
answer = 0
perm(0,[])
print(answer)

def perm(n, arr):
    global answer
    if n == 8:
        result, idx = 0, 0
        arr.insert(3,0)
        for inning in matrix:
            out = 0
            first, second, third = 0, 0, 0
            while out < 3:
                score = inning[arr[idx]]
                if score == 0:
                    out += 1
                elif score == 1:
                    result += third
                    first, second, third = 1, first, second
                elif score == 2:
                    result += second+third
                    first, second, third = 0, 1, first
                elif score == 3:
                    result += first+second+third
                    first, second, third = 0, 0, 1
                else:
                    result += first+second+third+1
                    first, second, third = 0, 0, 0
                idx = (idx+1)%9
        answer = max(answer, result)
        return
    else:
        for x in range(1,9):
            if not visited[x]:
                visited[x] = True
                perm(n+1, arr+[x])
                visited[x] = False

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [False]*9
answer = 0
perm(0,[])
print(answer)