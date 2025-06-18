from collections import deque

n, k = tuple(map(int, input().split()))

nums = list(map(int, input().split()))

mins_deque = deque([])

for i, num in enumerate(nums):
    while mins_deque:
        last_num = mins_deque[-1]
        if last_num <= num:
            break
        mins_deque.pop()

    mins_deque.append(num)
    if i >= k - 1:
        print(mins_deque[0])
        if nums[i - (k-1)] == mins_deque[0]:
            mins_deque.popleft()