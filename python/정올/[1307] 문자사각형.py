# https://www.jungol.co.kr/problem/1307

import string
alphabet = list(string.ascii_uppercase)

n = int(input())
idx = 0
matrix = [['' for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        matrix[n-j-1][n-i-1] = alphabet[idx]
        idx += 1
        if idx == 26:
            idx = 0
for row in matrix:
    print(' '.join(row))