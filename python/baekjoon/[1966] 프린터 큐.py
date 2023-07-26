# https://www.acmicpc.net/problem/1966
import sys

sys.stdin=open("input.txt", "rt")
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    answer = 1
    while len(arr):
        if len(list(filter(lambda x: x > arr[0], arr[1:]))):
            arr = arr[1:] + [arr[0]]
            if M == 0:
                M = len(arr)-1
            else:
                M -= 1
        else:
            if M == 0:
                print(answer)
                break
            else:
                arr.pop(0)
                M -= 1
                answer += 1