n, k = tuple(map(int, input().split()))
car_numbers = list(map(int, input().split()))
cnt, first, last = 0, 0, 0
nowsum = car_numbers[0]

for first in range(n):
    if first == last and nowsum == k:
        cnt += 1
        last += 1
        if last != n:
            nowsum = car_numbers[last]
        continue

    while last < n - 1 and nowsum < k:
        last += 1
        nowsum += car_numbers[last]

    if nowsum == k:
        cnt += 1

    nowsum -= car_numbers[first]

print(cnt)