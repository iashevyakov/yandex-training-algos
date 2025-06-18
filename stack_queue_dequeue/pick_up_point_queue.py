from collections import deque

n, b = tuple(map(int, input().split()))
a = list(map(int, input().split()))

cnt_queue = deque()
answer = 0

for i, cnt in enumerate(a):
    current_minute_processed = 0
    while cnt_queue and current_minute_processed < b:
        cnt_queue_item = cnt_queue.popleft()
        min_cnt = min(b, cnt_queue_item[0])
        item_ans = min_cnt * (i - cnt_queue_item[1] + 1)
        answer += item_ans
        current_minute_processed += min_cnt

        q_item_diff = cnt_queue_item[0] - b
        if q_item_diff > 0:
            cnt_queue.appendleft((q_item_diff, cnt_queue_item[1]))

    current_minute_rest = b - current_minute_processed
    answer += min(current_minute_rest, cnt) * 1

    q_value = cnt - current_minute_rest
    if q_value > 0:
        cnt_queue.append((q_value, i))

while cnt_queue:
    item = cnt_queue.popleft()
    answer += item[0] * (n - item[1] + 1)

print(answer)