# TODO: 투 포인터 안 보고 다시 풀어보기
# https://www.acmicpc.net/problem/3273
import sys
sys.stdin=open("input.txt", "rt")
input = sys.stdin.readline
N = int(input())
arr = sorted(list(map(int, input().split())))
X = int(input())
answer = 0
left, right = 0, N-1
while left < right:
    if arr[left] + arr[right] == X:
        answer += 1
        left += 1
    elif arr[left] + arr[right] < X:
        left += 1
    else:
        right -= 1
print(answer)