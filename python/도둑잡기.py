user_input = input()
dict = {}
for i in user_input.split():
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
for i in dict:
    if dict[i] == 1:
        print(i)
        break