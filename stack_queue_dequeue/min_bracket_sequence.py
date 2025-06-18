n = int(input())
ws = list(input())
s = input()

char_stack = []
opening_brackets = {'(', '['}
matching = {')': '(', ']': '['}
using_opening, using_closing = 0, 0
answer = s

for char in s:
    if char in opening_brackets:
        using_opening += 1
        char_stack.append(char)
    else:
        using_closing += 1
        char_stack.pop()

while using_opening + using_closing != n:
    for w in ws:
        if w not in opening_brackets and char_stack and char_stack[-1] == matching[w]:
            answer += w
            char_stack.pop()
            using_closing += 1
            break
        if w in opening_brackets and using_opening != n / 2:
            answer += w
            char_stack.append(w)
            using_opening += 1
            break

print(answer)