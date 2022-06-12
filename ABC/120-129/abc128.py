import sys

sys.stdin = open("input.txt")

# A
# a, p = map(int, input().split())
# print((a * 3 + p) // 2)


# B
n = int(input())
a = []
for i in range(n):
    s, p = input().split()
    a += [(s, -int(p), i + 1)]
a.sort()
{print(t[2]) for t in a}

# C
# import itertools
# n, m = [int(i) for i in input().split()]
# sss = [[int(i) for i in input().split()][1:] for _ in range(m)]
# ps = [int(i) for i in input().split()]
#
# ans = 0
# for pro in itertools.product((0, 1), repeat=n):
#     for ss, p in zip(sss, ps):
#         pp = sum(pro[s-1] for s in ss) % 2
#         if pp != p:
#             break
#     else:
#         ans += 1
#
# print(ans)

# D
# from bisect import bisect_left
#
# n, k = map(int, input().split())
# v = list(map(int, input().split()))
#
# ans = 0
# for i in range(0, k + 1):
#     for j in range(0, min(k, n) - i + 1):
#         tmp = v[:i] + (v[-j:] if j else [])
#         tmp.sort()
#         idx = min(k - i - j, bisect_left(tmp, 0))
#         ans = max(ans, sum(tmp[idx:]))
#
# print(ans)
