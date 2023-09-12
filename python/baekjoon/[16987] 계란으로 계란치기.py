# 1차 제출: 142764kb, 1480ms
# 2차 제출: 다 깨지면 조기 종료 (1480ms -> 1432ms)
# 3차 제출: 나머지를 다 깨도 최대값을 갱신할 수 없는 경우(if cnt + (N-n)*2 <= answer: return) 추가 (1432ms -> 708ms)
# https://www.acmicpc.net/problem/16987
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def dfs(n, cnt):
    global answer
    if cnt == N:
        answer = cnt
        return
    if cnt + (N-n)*2 <= answer: return
    if n == N:
        answer = max(cnt, answer)
        return
    for x in range(N):
        if n != x:
            egg1, egg2 = eggs[n], eggs[x]
            s1, w1 = egg1
            s2, w2 = egg2
            if s1 > 0 and s2 > 0:
                eggs[n], eggs[x] = [s1-w2, w1], [s2-w1, w2]
                if s1 > 0 and s1-w2 <= 0: cnt += 1
                if s2 > 0 and s2-w1 <= 0: cnt += 1
            dfs(n+1, cnt)
            if s1 > 0 and s2 > 0:
                if s1 > 0 and s1-w2 <= 0: cnt -= 1
                if s2 > 0 and s2-w1 <= 0: cnt -= 1
                eggs[n], eggs[x] = [s1, w1], [s2, w2]

N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]
answer = 0
dfs(0,0)
print(answer)