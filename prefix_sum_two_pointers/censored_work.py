n, c = tuple(map(int, input().split()))
s = input()

a_cnt = b_cnt = pen = 0
l = r = bestl = bestr = 0

while r < n:
    if pen <= c:
        if s[r] == 'a':
            a_cnt += 1
        elif s[r] == 'b':
            pen += a_cnt
            b_cnt += 1
    else:
        while pen > c:
            if s[l] == 'a':
                a_cnt -= 1
                pen -= b_cnt
            elif s[l] == 'b':
                b_cnt -= 1
            l += 1
    if pen <= c:
        if r - l > bestr - bestl:
            bestr, bestl = r, l
        r += 1

print(bestr - bestl + 1)
