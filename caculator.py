def calculate(inputs):
    stack = []
    for a in inputs:
        if type(a) is int:
            stack.append(a)
            continue
        # if(stack == []):
        #     continue
        # else:
        op1, op2 = stack.pop(), stack.pop()

        if a == '+':
            stack.append(op2 + op1)
        elif a == '-':
            stack.append(op2 - op1)
        elif a == '*':
            stack.append(op2 * op1)
        elif a == '/':
            stack.append(op2 / op1)


    return stack.pop()

calculate('10+65')
