# https://www.jungol.co.kr/problem/1828
# 회의실과 달리 많이 겹치는 것이 유리
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
N = int(input())
arr = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: (x[1], x[0]))
answer, temperature = 0, -270
while arr:
    low, high = arr.pop(0)
    while arr and arr[0][0] <= high:
        arr.pop(0)
    answer += 1
print(answer)

# 두번째 풀이
N = int(input())
arr = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: (x[1], x[0]))
answer, temperature = 1, arr.pop(0)[1]
for low, high in arr:
    if low > temperature:
        temperature = high
        answer += 1
print(answer)