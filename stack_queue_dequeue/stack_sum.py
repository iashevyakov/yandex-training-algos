n = int(input())

num_stack = []
prefix_sum = [0]


for i in range(n):
    op = input()
    if op[0] == '+':
        num = int(op[1:])
        num_stack.append(num)
        prefix_sum.append(prefix_sum[-1] + num)
    if op[0] == '-':
        prefix_sum.pop()
        print(num_stack.pop())
    if op[0] == '?':
        k = int(op[1:])
        prefix_len = len(prefix_sum)
        result_sum = prefix_sum[prefix_len - 1] - prefix_sum[prefix_len - 1 - k]
        print(result_sum)