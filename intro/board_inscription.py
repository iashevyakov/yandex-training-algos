n = int(input())
lst = [None] * n
for i in range(n):
    lst[n-i-1] = list(input())

def get_external_box():
    x1, x2 = 11, 0
    y1, y2 = 11, 0
    for y in range(n):
        for x in range(n):
            if lst[y][x] == '#':
                x2 = max(x2, x)
                x1 = min(x1, x)
                y1 = min(y1, y)
                y2 = max(y2, y)
    return x1, x2, y1, y2

def get_internal_box(x1, x2, y1, y2):
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            if lst[y][x] == '.':
                y3, x3, y4, x4 = y, x, y, x
                while y4 + 1 <= y2 and lst[y4 + 1][x] == '.':
                    y4 += 1
                while x4 + 1 <= x2 and lst[y][x4 + 1] == '.':
                    x4 += 1
                for y in range(y3, y4 + 1):
                    for x in range(x3, x4 + 1):
                        if lst[y][x] == '.':
                            lst[y][x] = '#'
                            continue
                        return "NO"
                return x3, x4, y3, y4


def get_result():
    x1, x2, y1, y2 = get_external_box()
    if x1 > x2:
        return "X"
    i_box = get_internal_box(x1, x2, y1, y2)
    if i_box is None:
        return "I"
    if i_box == "NO":
        return "X"
    x3, x4, y3, y4 = i_box
    i_box = get_internal_box(x1, x2, y1, y2)
    if i_box is None:
        if  x1 < x3 <= x4 == x2 and y1 < y3 <= y4 == y2:
            return "L"
        if x1 < x3 <= x4 < x2 and y1 < y3 <= y4 < y2:
            return "O"
        if x1 < x3 <= x4 == x2 and y1 < y3 <= y4 < y2:
            return "C"
        return "X"
    if i_box == "NO":
        return "X"
    x5, x6, y5, y6 = i_box
    i_box = get_internal_box(x1, x2, y1, y2)
    if i_box is None:
        if x1 < x3 == x5 <= x6 < x4 == x2 and y1 == y3 <= y4 < y5 <= y6 < y2:
            return "P"
        if x1 < x3 == x5 <= x4 == x6 < x2 and y1 == y3 <= y4 < y5 <= y6 == y2:
            return "H"
        return "X"
    return "X"

f = get_result()
print(f)