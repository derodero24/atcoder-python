import sys

sys.stdin = open("input.txt")


def input():
    return sys.stdin.readline().strip()


# A
# n, h, w = int(input()), int(input()), int(input())
# print((n-h+1)*(n-w+1))

# B
# n = int(input())
# a, b = [int(i) for i in input().split()]
# p = sorted([int(i) for i in input().split()])
# x = len([i for i in p if i <= a])
# y = len([i for i in p if a < i <= b])
# z = len([i for i in p if i > b])
# print(min(x, y, z))


# C
# h, w = [int(i) for i in input().split()]
# for i in range(h):
#     s =

# D
# import copy
# import numpy as np
# n, q = [int(i) for i in input().split()]
# As = sorted([int(i) for i in input().split()])
# print(As)
# for i in range(q):
#     x = int(input())
#     # As_tmp = copy.copy(As)
#     As_abs = sorted([(abs(a-x), i) for i, a in enumerate(As)])
#     print(As_abs)
#     ans, num = sum(As), 0
#     for a, j in As_abs:
#         print(ans, num)
#         if j < len(As) - num * 2 - 1:
#             ans -= As[j]
#             num += 1
#         if num == len(As) // 2:
#             break
#     print(ans)


#     As_abs = abs(As - x)
#     # print(As_abs)
#     ans = 0
#     while len(As_abs):
#         ans += As_tmp[-1]
#         # print(ans)
#         As_tmp = np.delete(As_tmp, -1)
#         As_abs = np.delete(As_abs, -1)
#         if not len(As_abs):
#             break
#         # ans += As[As_abs.index(min(As_abs))]
#         # idx = As_abs.index(min(As_abs))
#         idx = As_abs.argmin()
#         # idx = np.where()
#         # idx = np.where()
#         As_tmp = np.delete(As_tmp, idx)
#         As_abs = np.delete(As_abs, idx)
#         # print(As_abs)
#
#     print(ans)
