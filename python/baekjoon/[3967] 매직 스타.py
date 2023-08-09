# https://www.acmicpc.net/problem/3967
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def check(arr):
    if arr[0]+arr[2]+arr[5]+arr[7]\
    == arr[7]+arr[8]+arr[9]+arr[10]\
    == arr[0]+arr[3]+arr[6]+arr[10]\
    == arr[1]+arr[2]+arr[3]+arr[4]\
    == arr[1]+arr[5]+arr[8]+arr[11]\
    == arr[4]+arr[6]+arr[9]+arr[11]: return True
    else: return False

def dfs(arr):
    if 0 not in arr:
        if check(arr):
            return arr
    else:
        idx = arr.index(0)
        for x in range(1,13):
            if x not in arr:
                arr[idx] = x
                result = dfs(arr)
                if result: return arr
                arr[idx] = 0

star = [list(filter(lambda x: x != '', input().strip().split('.'))) for _ in range(5)]
star = [x for row in star for x in row]
star = list(map(lambda x: 0 if ord(x) == 120 else ord(x)-64, star))
x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12 = list(map(lambda x: chr(x+64), dfs(star)))
print(f'....{x1}....')
print(f'.{x2}.{x3}.{x4}.{x5}.')
print(f'..{x6}...{x7}..')
print(f'.{x8}.{x9}.{x10}.{x11}.')
print(f'....{x12}....')