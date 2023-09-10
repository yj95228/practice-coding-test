# https://www.acmicpc.net/problem/29725
import sys
input = sys.stdin.readline

matrix = [list(input().rstrip()) for _ in range(8)]
score = [0,0]
for r in range(8):
    for c in range(8):
        chess = matrix[r][c]
        if chess == '.': continue
        elif chess.isupper():
            if chess == 'P': score[0] += 1
            elif chess == 'N' or chess == 'B': score[0] += 3
            elif chess == 'R': score[0] += 5
            elif chess == 'Q': score[0] += 9
        else:
            if chess == 'p': score[1] += 1
            elif chess == 'n' or chess == 'b': score[1] += 3
            elif chess == 'r': score[1] += 5
            elif chess == 'q': score[1] += 9
print(score[0]-score[1])