# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRDL1aeugDFAUo
T = int(input())
dt = ((0,0),(-1,0),(0,1),(1,0),(0,-1))
# 모든 사용자가 충전한 양의 합의 최댓값
for tc in range(1, T+1):
    M, A = map(int, input().split())    # 총 이동 시간(20 <= M <= 100), BC의 개수(1 <= A <= 8)
    matrix = [[[] for _ in range(10)] for _ in range(10)]

    # 그 다음 2개의 줄에는 각각 사용자 A와 B의 이동 정보가 주어진다.
    arr = [[0] + list(map(int, input().split())) for _ in range(2)]

    # 하나의 BC 정보는 좌표(X, Y), 충전 범위(1 <= C <= 4), 처리량(10 <= P 짝수 <= 500)로 구성된다.
    charge = dict()
    for i in range(A):
        Y, X, C, P = map(int, input().split())
        charge[i] = P
        for r in range(10):
            for c in range(10):
                if abs(r-X+1)+abs(c-Y+1) <= C:
                    matrix[r][c].append(i)

    ar, ac, br, bc = 0, 0, 9, 9
    answer = 0
    for i in range(M+1):
        (dx1, dy1), (dx2, dy2) = dt[arr[0][i]], dt[arr[1][i]]
        nar, nac, nbr, nbc = ar+dx1, ac+dy1, br+dx2, bc+dy2
        result = 0
        lst1, lst2 = matrix[nar][nac], matrix[nbr][nbc]
        if not lst1 and not lst2:
            ar, ac, br, bc = nar, nac, nbr, nbc
        elif not lst1:
            for j in lst2:
                result = max(result, charge[j])
        elif not lst2:
            for j in lst1:
                result = max(result, charge[j])
        else:
            for x in lst1:
                for y in lst2:
                    if x == y:
                        result = max(result, charge[x]//2+charge[y]//2)
                    else:
                        result = max(result, charge[x]+charge[y])
        answer += result
        ar, ac, br, bc = nar, nac, nbr, nbc
    print(f'#{tc} {answer}')