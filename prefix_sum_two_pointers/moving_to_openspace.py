n = int(input())
a = list(map(int, input().split()))

result = float('inf')
prefix = [0] * n

prefix[0] = a[0]
for i in range(1, n):
    prefix[i] = prefix[i - 1] + a[i]

prefix_left = [0] * n
for i in range(1, n):
    prefix_left[i] = prefix_left[i - 1] + prefix[i - 1]

prefix = [0] * n
prefix[0] = a[n - 1]
for i in range(n - 2, -1, -1):
    prefix[n - i - 1] = prefix[n - i - 2] + a[i]

prefix_right = [0] * n
for i in range(1, n):
    prefix_right[i] = prefix_right[i - 1] + prefix[i - 1]

for i in range(0, n):
    result = min(result, prefix_left[i] + prefix_right[n - i - 1])

print(result)
