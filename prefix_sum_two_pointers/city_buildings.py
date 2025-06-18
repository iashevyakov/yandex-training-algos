n, r = tuple(map(int, input().split()))
dist = list(map(int, input().split()))
first, last = 0, 1
cnt = 0

for first in range(n):
    while last < n and dist[last] - dist[first] <= r:
        last += 1

    cnt += n - last

print(cnt)