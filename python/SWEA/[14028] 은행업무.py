# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmCPbwakowDFAUe&contestProbId=AX9W7RO6E9QDFAQe&probBoxId=AYoWpgnai9cDFARi&type=USER&problemBoxTitle=20_230821%3A+%EC%97%B0%EC%8A%B5_01&problemBoxCnt=2
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    two = input().rstrip()
    three = input().rstrip()
    twotwo = [2**x for x in range(len(two))][::-1]
    threethree = [3**x for x in range(len(three))][::-1]
    two_list, three_list = set(), set()
    queue = [(0,x,0) for x in range(len(two))]
    while queue:
        idx, error, sm = queue.pop(0)
        if idx == len(two):
            two_list.add(sm)
        else:
            if idx == error:
                queue.append((idx+1, error, sm + twotwo[idx]*(0 if two[idx] == '1' else 1)))
            else:
                queue.append((idx+1, error, sm + twotwo[idx]*int(two[idx])))
    queue = [(0,x,0) for x in range(len(three))]
    while queue:
        idx, error, sm = queue.pop(0)
        if idx == len(three):
            three_list.add(sm)
        else:
            if idx == error:
                if three[idx] == '0':
                    queue.append((idx+1, error, sm + threethree[idx]))
                    queue.append((idx+1, error, sm + threethree[idx]*2))
                elif three[idx] == '1':
                    queue.append((idx+1, error, sm))
                    queue.append((idx+1, error, sm + threethree[idx]*2))
                elif three[idx] == '2':
                    queue.append((idx+1, error, sm))
                    queue.append((idx+1, error, sm + threethree[idx]))
            else:
                queue.append((idx+1, error, sm + threethree[idx]*int(three[idx])))
    print(f'#{tc} {two_list.intersection(three_list).pop()}')