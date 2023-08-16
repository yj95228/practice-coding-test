# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX_0cHyqaNwDFAVy&probBoxId=AYn7aaSaYAgDFARi&type=USER&problemBoxTitle=17_230816%3A+%EA%B7%B8%EB%9E%98%ED%94%84%ED%99%9C%EC%9A%A9&problemBoxCnt=5
import sys
sys.stdin = open('input.txt', 'r')

# 노드 N의 대표자 번호를 return
def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

# B가 속한 그룹을 A 그룹의 대표자 번호로 설정
def union(a,b):
    parents[find(b)] = find(a)

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    answer = 0
    # [1] make set (각자대표인 parents[] 생성) 1~N
    parents = [x for x in range(N+1)]
    # [2] union(a,b): B가 속한 그룹을 A가 속한 그룹과 합침
    # B의 그룹 대표자의 부모 <- A의 그룹 대표자
    # [3] find: 그룹의 대표자를 return
    for i in range(0, len(arr), 2):
        union(arr[i], arr[i+1])
    # parents[]에서 index 값이 같으면 그룹 대표 == 그룹 개수
    for i in range(1,N+1):
        if i == parents[i]: answer += 1
    print(f'#{tc} {answer}')