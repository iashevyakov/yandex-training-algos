A = int(input())
B = int(input())
C = int(input())
D = int(input())

results = []
if A != 0 and B != 0:
    results.append((max(A, B) + 1, 1))
if C != 0 and D != 0:
    results.append((1, max(C, D) + 1))
if A != 0 and C != 0:
    results.append((B + 1, D + 1))
if B != 0 and D != 0:
    results.append((A + 1, C + 1))

result = min(results, key=sum)

print(result[0], result[1])