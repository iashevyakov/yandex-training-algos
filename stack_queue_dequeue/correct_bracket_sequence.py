seq = input()

opening_brackets = {'(', '[', '{'}
matching = {')': '(', ']': '[', '}': '{'}

char_stack = []

def check_if_right_bracket_seq(seq: str):
    for char in seq:
        if char in opening_brackets:
            char_stack.append(char)
        else:
            if not char_stack:
                return "no"
            if char_stack.pop() != matching[char]:
                return "no"

    return "no" if char_stack else "yes"

print(check_if_right_bracket_seq(seq))