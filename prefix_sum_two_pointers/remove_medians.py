n = int(input())
a = list(map(int, input().split()))

a.sort()

if n % 2 == 1:
    mid = n // 2
    left, right = mid - 1, mid
else:
    left = n // 2 - 1
    right = left + 1

o = []
k = n
while k != 0:
    if k % 2 == 1:
        o.append(a[right])
        right += 1
    else:
        o.append(a[left])
        left -= 1
    k -= 1

print(*o, sep=' ')
