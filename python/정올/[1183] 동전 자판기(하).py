# https://www.jungol.co.kr/problem/1183
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
W = int(input())
arr = list(map(int, input().split()))
coins = [500,100,50,10,5,1]
result = [0]*6
answer = []
total = 0
for i in range(6):
    total += coins[i]*arr[i]
target = total - W
for i in range(6):
    mok, namuji = divmod(target, coins[i])
    result[i] = mok
    target = namuji
for i in range(6):
    answer.append(arr[i]-result[i])
print(sum(answer))
print(*answer)