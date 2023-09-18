import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
answer, result = 0, 0
for x in arr:
    if x == 0:
        result = 0
    else:
        result += 1
        answer = max(result, answer)
print(answer)