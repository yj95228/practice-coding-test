# https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = ''
    left = '*'
    right = '#'
    keypad = [[1,4,7,'*'],[2,5,8,0],[3,6,9,'#']]
    for i in range(len(numbers)):
        if numbers[i] in keypad[0]:
            answer += 'L'
            left = numbers[i]
        elif numbers[i] in keypad[2]:
            answer += 'R'
            right = numbers[i]
        else:
            ydist = keypad[1].index(numbers[i])
            left_point = [[i,j] for i in range(len(keypad)) for j in range(len(keypad[i])) if keypad[i][j] == left][0]
            right_point = [[i,j] for i in range(len(keypad)) for j in range(len(keypad[i])) if keypad[i][j] == right][0]
            left_dist = abs(1 - left_point[0]) + abs(ydist - left_point[1])
            right_dist = abs(1 - right_point[0]) + abs(ydist - right_point[1])
            if left_dist < right_dist:
                answer += 'L'
                left = numbers[i]
            elif left_dist > right_dist:
                answer += 'R'
                right = numbers[i]
            else:
                if hand == 'left':
                    answer += 'L'
                    left = numbers[i]
                else:
                    answer += 'R'
                    right = numbers[i]
    return answer
