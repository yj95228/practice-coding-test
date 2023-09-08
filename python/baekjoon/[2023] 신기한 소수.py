# https://www.acmicpc.net/problem/2023
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def is_prime(n):
    for x in range(2,int(n**(1/2))+1):
        if n % x == 0:
            return False
    return True

def dfs(n, num):
    if n == N:
        print(num)
        return
    for x in [1,3,5,7,9]:
        if is_prime(10*num+x):
            dfs(n+1, 10*num+x)

N = int(input())
answer = []
dfs(1, 2)
dfs(1, 3)
dfs(1, 5)
dfs(1, 7)