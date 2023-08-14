# https://www.acmicpc.net/problem/1912
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))[::-1]
answer, mx = 0, 0
for i in range(1,N):
    arr[i] = max(arr[i], arr[i]+arr[i+1])
print(max(arr))