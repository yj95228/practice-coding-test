# 1차 제출: 실패 (문자열 뒤집는걸 A -> B, B -> A로 잘못 이해함)
# 2차 제출: 실패 (문자열 pop하고 마지막 글자 확인하면 무슨 소용인가)
# 3차 제출: 113112kb, 124ms
# https://www.acmicpc.net/problem/12904
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

S = input().rstrip()
T = list(input().rstrip())
while len(T) > len(S):
    if T.pop() == 'B':
        T = T[::-1]
print(1 if S == ''.join(T) else 0)
