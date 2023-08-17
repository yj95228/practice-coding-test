# https://www.acmicpc.net/problem/1244
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
K = int(input())
for _ in range(K):
    gender, num = map(int, input().split())
    if gender == 1:
        for i in range(1,N//num+1):
            arr[i*num-1] = 0 if arr[i*num-1] else 1
    else:
        mn = min(num, N-num+1)
        for i in range(mn):
            if i == 0:
                arr[num-1] = 0 if arr[num-1] else 1
            else:
                if arr[num-1+i] == arr[num-1-i]:
                    arr[num-1+i] = 0 if arr[num-1+i] else 1
                    arr[num-1-i] = 0 if arr[num-1-i] else 1
                else:
                    break
for m in range((N+20)//20):
    print(*arr[20*m:20*(m+1)])