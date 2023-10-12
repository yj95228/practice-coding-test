# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeV9sKkcoDFAVH
def rotate(num, dt, start):
    if start <= 0 and 0 <= num-1 and matrix[num-1][2] != matrix[num][6]:
        rotate(num-1, -dt, -1)
    if start >= 0 and num+1 < 4 and matrix[num][2] != matrix[num+1][6]:
        rotate(num+1, -dt, 1)
    if dt == 1:
        matrix[num] = [matrix[num][-1]] + matrix[num][:-1]
    else:
        matrix[num] = matrix[num][1:] + [matrix[num][0]]

T = int(input())
for tc in range(1, T+1):
    K = int(input())
    matrix = [list(map(int, input().split())) for _ in range(4)]
    for _ in range(K):
        num, dt = map(int, input().split())
        rotate(num-1, dt, 0)
    print(f'#{tc} {sum([x * y for x, y in zip([row[0] for row in matrix], [1, 2, 4, 8])])}')