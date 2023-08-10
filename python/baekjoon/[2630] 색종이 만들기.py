# https://www.acmicpc.net/problem/2630
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def check(matrix):
    return all(list(map(all, matrix)))\
    or not any(list(map(any, matrix)))

def solve(matrix):
    if check(matrix) or len(matrix) == 1:
        answer[matrix[0][0]] += 1
        return
    n = len(matrix)//2
    solve([row[:n] for row in matrix[:n]])
    solve([row[n:] for row in matrix[:n]])
    solve([row[:n] for row in matrix[n:]])
    solve([row[n:] for row in matrix[n:]])

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
answer = [0,0]
solve(matrix)
print(*answer, sep='\n')