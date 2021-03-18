# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []
    stud1 = []
    stud2 = []
    stud3 = []
    question = len(answers)
    answer1 = 0
    answer2 = 0
    answer3 = 0
    
    stu1 = [1,2,3,4,5]
    for i in range(question//5+1):
        stud1 += stu1
    stud1 = stud1[0:question]
    
    stu2 = [2,1,2,3,2,4,2,5]
    for i in range(question//8+1):
        stud2 += stu2
    stud2 = stud2[0:question]
    
    stu3 = [3,3,1,1,2,2,4,4,5,5]
    for i in range(question//10+1):
        stud3 += stu3
    stud3 = stud3[0:question]
    
    for i in range(question):
        if stud1[i] == answers[i]:
            answer1 += 1
        if stud2[i] == answers[i]:
            answer2 += 1
        if stud3[i] == answers[i]:
            answer3 += 1
    
    answerlist = [answer1,answer2,answer3]
    maxanswer = max(answerlist)
    answer = [i+1 for i, j in enumerate(answerlist) if j == maxanswer]
    
    return answer
