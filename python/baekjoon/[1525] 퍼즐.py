import sys

input = sys.stdin.readline


def solve(arr):
    queue = [(0, arr)]
    while queue:
        temp_q = []
        for turn, a in queue:
            if a == '123456780': return turn

            A = list(a)
            idx = A.index('0')

            for dx in [-3, -1, 1, 3]:
                if idx % 3 == 0 and dx == -1:
                    continue
                elif idx % 3 == 2 and dx == 1:
                    continue
                B = A[:]
                nx = idx + dx
                if 0 <= nx < 9:
                    B[nx], B[idx] = A[idx], A[nx]
                    num = ''.join(B)
                    if num in V: continue
                    V.add(num)
                    temp_q.append((turn + 1, num))

        queue = temp_q

    return -1


A = ''.join([''.join(input().split()) for _ in range(3)])
V = set()
V.add(A)
print(solve(A))