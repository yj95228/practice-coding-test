import sys

sys.stdin=open("python\백준\input.txt","rt")
input = sys.stdin.readline
print(sum(map(int,input().split())))