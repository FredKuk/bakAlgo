import sys
n, m = map(int, sys.stdin.readline().split())
number = list(map(int, sys.stdin.readline().split()))
sum_number = [0] * (n + 1)
tmp = 0
for i in range(n):
    tmp += number[i]
    sum_number[i+1] = tmp
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(sum_number[b-1+1] - sum_number[a-1])