# https://www.acmicpc.net/problem/1259
import sys

sys.stdin = open('input.txt','rt')
input = sys.stdin.readline

while True:
    x = input().strip()
    if x == '0': break
    print('yes' if ''.join(list(x)) == ''.join(list(x)[::-1]) else 'no')