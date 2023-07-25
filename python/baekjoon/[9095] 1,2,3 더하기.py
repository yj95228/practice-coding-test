import sys

sys.stdin=open("python\백준\input.txt","rt")
input = sys.stdin.readline
N = int(input())
data = []
for i in range(N):
    data.append(int(input()))
M = max(data)
d = [0]*(M+1)
d[1] = 1
d[2] = 2
d[3] = 4
for i in range(4,M+1):
    d[i] = sum([d[i-1],d[i-2],d[i-3]])
for i in list(map(lambda x: d[x], data)):
    print(i)