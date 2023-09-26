import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
left, right = 0, N-1
answer = 2_000_000_000
a1, a2 = None, None
while left < right:
    result = arr[left]+arr[right]
    if abs(result) < answer:
        answer = abs(result)
        a1, a2 = left, right
    if result < 0:
        left += 1
    elif result > 0:
        right -= 1
    else:
        a1, a2 = left, right
        break
print(arr[a1], arr[a2])