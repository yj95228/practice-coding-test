# https://www.acmicpc.net/problem/4577
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N = int(input())
dp = [0,1,1]
for i in range(len(dp),N+1):
    dp.append(dp[-1]+dp[-2])
print(dp[-1])