n, k = tuple(map(int, input().split()))
a = list(map(int, input().split()))

a.sort()
result, first = 1, 0

for last in range(n):
    if a[last] - a[first] > k:
        result = max(last - first, result)
        first += 1

result = max(n - first, result)

print(result)