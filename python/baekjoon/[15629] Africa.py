import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
arr = [input().rstrip() for _ in range(N)]
answer = 0

if 'namibia' in arr:
    if 'south-africa' in arr and arr.index('south-africa') < arr.index('namibia'):
        answer += 40
    else:
        answer += 140

if 'zimbabwe' in arr and 'zambia' in arr and\
    (arr.index('zimbabwe')+1 == arr.index('zambia') or arr.index('zimbabwe') == arr.index('zambia')+1):
    answer += 50
else:
    if 'zimbabwe' in arr:
        answer += 30
    if 'zambia' in arr:
        answer += 50

if 'tanzania' in arr:
    answer += 50

if 'ethiopia' in arr:
    answer += 50

if 'kenya' in arr:
    answer += 50

print(answer)