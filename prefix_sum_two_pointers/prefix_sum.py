n = int(input())
a = list(map(int, input().split()))
sums = [0] * (n + 1)
for i in range(1, n + 1):
    sums[i] = sums[i - 1] + a[i - 1]

print(*sums[1:], sep=' ')