# https://www.acmicpc.net/problem/1978
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def is_prime(x):
    if x == 1: return 0
    else:
        for i in range(2,int(x**(1/2))+1):
            if x%i == 0: return 0
    return 1

N = int(input())
arr = list(map(int, input().split()))
answer = 0
for x in arr:
    answer += is_prime(x)
print(answer)