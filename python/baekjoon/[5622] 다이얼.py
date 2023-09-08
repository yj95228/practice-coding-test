# https://www.acmicpc.net/problem/5622
# FIXME: dictionary 대신에 list idx로 풀수도 있었음
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

txt = list(input().rstrip())
abc = {x:3 for x in 'ABC'}
def_ = {x:4 for x in 'DEF'}
ghi = {x:5 for x in 'GHI'}
jkl = {x:6 for x in 'JKL'}
mno = {x:7 for x in 'MNO'}
pqrs = {x:8 for x in 'PQRS'}
tuv = {x:9 for x in 'TUV'}
wxyz = {x:10 for x in 'WXYZ'}
dial = {**abc, **def_, **ghi, **jkl, **mno, **pqrs, **tuv, **wxyz}
answer = 0
for x in txt:
    answer += dial[x]
print(answer)