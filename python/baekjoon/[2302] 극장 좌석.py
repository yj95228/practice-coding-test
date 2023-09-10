# 1차 제출: DFS (시간초과)
# 2차 제출: 피보나치 규칙 맞는지 모르겠는데 일단 제출해봄
# 3차 제출: 0으로 곱해지는 경우 없애주기 (113112kb 112ms)
# https://www.acmicpc.net/problem/2302
import sys
sys.stdin = open('python/baekjoon/input.txt','r')
input = sys.stdin.readline

def fibo(n):
    for _ in range(len(arr)-1,n):
        arr.append(arr[-1] + arr[-2])
    return arr[n]

N = int(input())
M = int(input())
arr = [0,1,2]
vip = [0] + [int(input()) for _ in range(M)] + [N+1]
answer = 1
for v in range(1,len(vip)):
    answer *= max(1, fibo(vip[v]-vip[v-1]-1))
print(answer)