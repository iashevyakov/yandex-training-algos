from collections import deque

row = input()
postfix_answer = []
digit_deque = deque()
char_deque = deque()


def digits_to_answer():
    num = ''
    while digit_deque:
        num += digit_deque.popleft()
    postfix_answer.append(int(num))


def push_char_to_answer(chars):
    while char_deque:
        last_deque_char = char_deque[-1]
        if last_deque_char in chars:
            postfix_answer.append(char_deque.pop())
        else:
            break


def preprocess_row(row: str):
    new_row = ''
    row = row.strip()
    if row[0] in ('+', '-'):
        new_row += '0'

    for i, c in enumerate(row):
        new_row += c
        if c == '(' and i != len(row) - 1 and row[i + 1] in ('+', '-'):
            new_row += '0'

    return new_row


def process_row(row: str):
    if not row:
        return "WRONG"

    row = preprocess_row(row)

    for i, char in enumerate(row):

        if not char in ('(', ')', ' ', '+', '-', '*') and not char.isdigit():
            return "WRONG"

        if char.isdigit():
            if i > 0:
                if digit_deque and row[i - 1] in (' ', '(', ')'):
                    return "WRONG"
                elif not digit_deque and row[i - 1] == ')':
                    return "WRONG"

            digit_deque.append(char)

        if char == '*':
            if digit_deque:
                digits_to_answer()
            push_char_to_answer(('*',))
            char_deque.append(char)

        if char in ('+', '-'):
            if digit_deque:
                digits_to_answer()

            push_char_to_answer(('+', '-', '*'))

            char_deque.append(char)

        if char == '(':
            if digit_deque:
                return "WRONG"

            char_deque.append(char)

        if char == ')':

            if digit_deque:
                digits_to_answer()

            if i > 0 and row[i - 1] in ('+', '-', '*', '('):
                return "WRONG"

            if not char_deque:
                return "WRONG"

            while char_deque:
                last_deque_char = char_deque.pop()
                if last_deque_char == '(':
                    break
                else:
                    postfix_answer.append(last_deque_char)
            else:
                return "WRONG"

    if digit_deque:
        digits_to_answer()

    while char_deque:
        postfix_answer.append(char_deque.pop())

    return postfix_answer


def calc_value(answer):
    digit_stack = []

    for char in answer:
        if isinstance(char, int):
            digit_stack.append(char)
        else:
            try:
                a, b = digit_stack.pop(), digit_stack.pop()
                if char == '+':
                    res = b + a
                elif char == '-':
                    res = b - a
                else:
                    res = b * a
                digit_stack.append(res)
            except:
                return "WRONG"

    return digit_stack[0]


answer = process_row(row)
if answer != "WRONG":
    print(calc_value(answer))
else:
    print(answer)
