# https://www.acmicpc.net/problem/1747
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def is_palindrome(x):
    return True if ''.join(x) == ''.join(x[::-1]) else False

def is_prime(x):
    for i in range(2,int(x**(1/2))+1):
        if x%i == 0:
            return False
    return True

N = int(input())
if N == 2: print(N)
elif N == 1: print(2)
else:
    if N%2 == 0: N += 1
    while not (is_palindrome(list(str(N))) and is_prime(N)):
        N += 2
    print(N)