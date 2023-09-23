# https://www.acmicpc.net/problem/16637
import sys
sys.stdin = open('python/baekjoon/input.txt','r')
input = sys.stdin.readline

def calc(lst):
    result = lst.pop(0)
    while lst:
        c = lst.pop(0)
        if c == '+':
            result += lst.pop(0)
        elif c == '-':
            result -= lst.pop(0)
        else:
            result *= lst.pop(0)
    return result

def recur(n, arr):
    global answer
    if n > N:
        lst = []
        i = 0
        while True:
            if i == N+4:
                answer = max(calc(lst), answer)
                break
            if i+1 in arr:
                if txt[i+1] == '+':
                    lst.append(txt[i]+txt[i+2])
                elif txt[i+1] == '-':
                    lst.append(txt[i]-txt[i+2])
                else:
                    lst.append(txt[i]*txt[i+2])
                lst.append(txt[i+3])
                i += 4
            else:
                lst.append(txt[i])
                i += 1
        return
    
    if not arr or arr[-1]+2 < n:
        recur(n+4, arr+[n])
    recur(n+2, arr)

N = int(input())
txt = [0, '+'] + list(map(lambda x: int(x) if x.isdigit() else x, input().rstrip())) + ['+', 0]
answer = -9876543210
recur(1, [])
print(answer)