def calculator(user_input):
    user_input = user_input.split(" = ")
    user_input[0] = user_input[0].split(" ")
    print(user_input)
    num1 = int(user_input[0][0])
    num2 = int(user_input[0][2])
    
    if user_input[0][1] == "+":
        left = num1 + num2
    else:
        left = num1 - num2
    
    if left == int(user_input[-1]):
        return True
    else:
        return False

def solution(quiz):
    answer = []
    for q in quiz:
        if calculator(q):
            answer.append("O")
        else:
            answer.append("X")
    return answer