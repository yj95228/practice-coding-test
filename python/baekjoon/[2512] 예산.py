# https://www.acmicpc.net/problem/2512
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
left, right = 0, max(arr)
answer = 0
while left <= right:
    mid = (left+right)//2
    if sum(map(lambda x: x if x <= mid else mid, arr)) <= M:
        answer = mid
        left = mid+1
    else:
        right = mid-1
print(answer)