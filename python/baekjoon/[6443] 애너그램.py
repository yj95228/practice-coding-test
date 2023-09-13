# 1차 제출: 시간 초과
# 2차 제출: visited로 룩업테이블 사용 -> 시간초과
# 3차 제출: recur 돌면서 만든 결과물도 같이 매개변수로 넣기
# 4차 제출: 알파벳별 횟수 룩업테이블 사용 (153940kb, 572ms)
# 5차 제출: answer를 set이 아닌 리스트에 담기 (572ms -> 476ms)
# https://www.acmicpc.net/problem/6443
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def recur(n, arr, result):
    if n == length:
        answer.add(result)
        return
    for x in s:
        if alphabet[x]:
            alphabet[x] -= 1
            recur(n+1, arr+[x], result+chr(x+ord('a')))
            alphabet[x] += 1

N = int(input())
for _ in range(N):
    txt = input().rstrip()
    length = len(txt)
    alphabet = [0]*26
    s = set()
    answer = set()
    for x in txt:
        t = ord(x)-ord('a')
        s.add(t)
        alphabet[t] += 1
    recur(0,[],'')
    print(*sorted(answer), sep='\n')