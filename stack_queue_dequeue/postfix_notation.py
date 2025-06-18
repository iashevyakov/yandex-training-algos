row = input().strip().split(' ')

digit_stack = []

for char in row:
    if char.isdigit():
        digit_stack.append(int(char))
    else:
        a, b = digit_stack.pop(), digit_stack.pop()
        if char == '+':
            res = b + a
        elif char == '-':
            res = b - a
        else:
            res = b * a
        digit_stack.append(res)

print(digit_stack[0])