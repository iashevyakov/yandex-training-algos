n = int(input())

a = list(map(int, input().split()))
MOD = 1000000007
result, s = 0, 0

sums = []
for i in range(n):
    s += a[i]
    s %= MOD
    sums.append(s)

for i in range(1, n - 1):
    value_1 = a[i] * sums[i - 1] % MOD
    value_2 = sums[n - 1] - sums[i] % MOD
    result += (value_1 * value_2) % MOD
    result %= MOD

print(result)