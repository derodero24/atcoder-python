import sys

sys.stdin = open("input.txt")

# A
# a, b = [int(c) for c in input().split()]
# if a < 6:
#     print(0)
# elif a < 13:
#     print(b // 2)
# else:
#     print(b)

# B
# r, d, x = [int(c) for c in input().split()]
# for i in range(10):
#     x = r * x - d
#     print(x)

# C
# n, m = [int(c) for c in input().split()]
# lr = [[int(c) for c in input().split()] for _ in range(m)]
# ls, rs = zip(*lr)
# if min(rs) < max(ls):
#     print(0)
# else:
#     print(min(rs) - max(ls) + 1)

# D
# n, m = [int(c) for c in input().split()]
# A = {}
# for a in input().split():
#     a = int(a)
#     A[a] = A.get(a, 0) + 1
# # print(A)
#
# for i in range(m):
#     b, c = [int(c) for c in input().split()]
#     A[c] = A.get(c, 0) + b
# # print(A)
#
# A = sorted([(k, v) for k, v in A.items()], reverse=True)
# ans, num = 0, n
# for k, v in A:
#     # print(k, v, min(num, v))
#     ans += k * min(num, v)
#     num -= min(num, v)
#     if num == 0:
#         break
# print(ans)

# E
