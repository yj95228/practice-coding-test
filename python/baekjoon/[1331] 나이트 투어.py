# https://www.acmicpc.net/problem/1331
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

s = set()
chess = []
for i in range(36):
    night = input()
    r = ord(night[0])-ord('A')
    c = int(night[1])-1
    s.add((r,c))
    if i:
        if (chess[-1][0]-r, chess[-1][1]-c) not in ((-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2)):
            print('Invalid')
            break
        if len(s) != i+1:
            print('Invalid')
            break
    chess.append((r,c))
else:
    if (chess[-1][0]-chess[0][0], chess[-1][1]-chess[0][1]) not in ((-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2)):
        print('Invalid')
    else:
        print('Valid')