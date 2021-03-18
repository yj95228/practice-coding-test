# https://programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    answer = list(s)
    i = 0
    flag = True
    while i < len(answer):
        if answer[i] != " ":
            if flag == True:
                answer[i] = answer[i].upper()
                print(i,flag,answer[i])
                i += 1
                flag = False
            else:
                answer[i] = answer[i].lower()
                print(i,flag,answer[i])
                i += 1
                flag = True
        else:
            print(i,flag,answer[i])
            i += 1
            flag = True
    answer = ''.join(answer)
    return answer
