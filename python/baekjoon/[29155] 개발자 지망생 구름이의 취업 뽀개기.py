# https://www.acmicpc.net/problem/29155
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N = int(input())
p_list = [0] + list(map(int, input().split()))
q_list = [[] for _ in range(6)]
for _ in range(N):
    p, k = map(int, input().split())
    q_list[p].append(k)
answer = 0
for x in range(1,6):
    if not q_list[x]: continue
    q_list[x].sort()
    tmp = q_list[x][0]
    cnt = p_list[x]
    for k in q_list[x]:
        cnt -= 1
        answer += k+(k-tmp)
        tmp = k
        if not cnt: break
    answer += 60
print(answer-60)

# 첫 제출 때는 obj로 만들었는데 룩업테이블이 좀 더 빠름
N = int(input())
p_list = list(map(int, input().split()))
obj = {x:[] for x in range(1,6)}
for _ in range(N):
    p, k = map(int, input().split())
    obj[p].append(k)
answer = 0
for x in obj.keys():
    obj[x].sort()
    tmp = obj[x][0]
    cnt = 0
    for k in obj[x]:
        cnt += 1
        answer += k+(k-tmp)
        tmp = k
        if cnt >= p_list[x-1]: break
    answer += 60
print(answer-60)