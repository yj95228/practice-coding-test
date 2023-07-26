# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14hwZqABsCFAYD&categoryId=AV14hwZqABsCFAYD&categoryType=CODE&problemTitle=1220&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
def get_dead_lock2(m_map):
    size = len(m_map)
    cnt = 0
    for c in range(size):
        before = '0'
        for r in range(size):
            if m_map[r][c] == '0': continue
            elif m_map[r][c] == '2' and before == '1': cnt += 1
            before = m_map[r][c]
    return cnt

for tc in range(1, 11):
    T = int(input())
    answer = 0
    arr = [list(input().split()) for _ in range(T)]
    matrix = [[0 for i in range(100)] for col in range(100)]
    for i in range(100):
        for j in range(100):
            matrix[j][i] = arr[i][j]
    for arr in matrix:
        if len(set(arr)) == 3:
            lst = list(filter(lambda x: x != '0', arr))
            while lst[0] == '2' or lst[len(lst)-1] == '1':
                if lst[0] == '2':
                    lst.pop(0)
                if lst[len(lst)-1] == '1':
                    lst.pop()
            if lst:
                txt = ''.join(lst)
                num = 0
                for i, v in enumerate(txt):
                    if i > 0 and txt[i] != txt[i-1]:
                        num += 1
                answer += (num+1)/2
    print(f'#{tc} {int(answer)}')