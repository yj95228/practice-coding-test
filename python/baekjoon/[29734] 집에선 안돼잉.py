# https://www.acmicpc.net/problem/29734
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
T, S = map(int, input().split())
Zip = N+(N-1)//8*S
Dok = T+M+(M-1)//8*(T+S+T)
print('Zip' if Zip < Dok else 'Dok')
print(Zip if Zip < Dok else Dok)