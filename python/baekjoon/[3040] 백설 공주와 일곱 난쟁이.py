# https://www.acmicpc.net/problem/3040
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

arr = [int(input()) for _ in range(9)]
sm = sum(arr)
def solve():
    for i in range(8):
        for j in range(i+1,9):
            if arr[i]+arr[j] == sm-100:
                arr.remove(arr[j])
                arr.remove(arr[i])
                return
solve()
for x in arr:
    print(x)