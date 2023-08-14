# https://www.acmicpc.net/problem/2747
import sys
sys.stdin = open('input.txt','r')

input = sys.stdin.readline
N = int(input())
arr = [0,1]
for x in range(2,N+1):
    arr.append(arr[x-1]+arr[x-2])
print(arr[N])

# 강사님 코드
dp = [0]*(N+1)                  # [1] dp 테이블 생성
dp[1] = 1                       # [2] 초기값 설정
for i in range(2, N+1):         # [3] 반복 처리(범위)
    dp[i] = dp[i-1] + dp[i-2]   # [4] 점화식
print(dp[N])