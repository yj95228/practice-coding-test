# https://www.acmicpc.net/problem/18511
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def dfs(result):
    if result > N: return
    else:
        s.add(result)
    for x in arr:
        dfs(result*10+x)

N, K = map(int, input().split())
arr = list(map(int, input().split()))
s = set()
dfs(0)
print(max(s))