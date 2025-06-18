x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x = int(input())
y = int(input())

if x < x1:
    if y < y1:
        print("SW")
    elif y1 < y < y2:
        print("W")
    else:
        print("NW")
elif x1 < x < x2:
    if y > y2:
        print("N")
    else:
        print("S")
else:
    if y > y2:
        print("NE")
    elif y1 < y < y2:
        print("E")
    else:
        print("SE")