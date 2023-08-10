# https://www.acmicpc.net/problem/1920
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def binary_search(left, right, v):
    while left <= right:
        mid = (left+right)//2
        if A[mid] == v:
            return 1
        elif A[mid] < v:
            left = mid+1
        else:
            right = mid-1
    return 0

N = int(input())
A = sorted(map(int, input().split()))
M = int(input())
arr = map(int, input().split())
for x in arr:
    print(binary_search(0, len(A)-1, x))

# 이진 탐색이 아닌 set으로 찾는 방법 (더 빠름)
N = int(input())
arr = set(map(int, input().split()))
M = int(input())
arr2 = tuple(map(int, input().split()))
print(*[1 if x in arr else 0 for x in arr2], sep='\n')