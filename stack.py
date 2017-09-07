arr = input()
array = []
stack = []

def push(char):
    array.append(char)
def pop():
    array.pop(-1)

for i in arr:
    array.append(i)

for b in array:
    count = 0
    if(b =='*'):
        push(stack.append(array[count-1]))
        push(stack.append(array[count+1]))
        a = stack.pop()
        b = stack.pop()
        c = stack.append(a * b)
    count += 1





