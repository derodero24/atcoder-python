import sys

sys.stdin = open("input.txt")


def input():
    return sys.stdin.readline().strip()


# A
# ans, w_idx = 0, 0
# for i, s in enumerate(input()):
#     if s != 'W':
#         continue
#     ans += i - w_idx
#     w_idx += 1
# print(ans)


# B
import math

N = int(input())
A = sorted([int(i) for i in input().split()], reverse=True)
dp = {}
for a in A:
    # print(dp.get(a, 0), dp)
    dp[a] = dp.get(a, 0) + 1
# print(A, dp)
ans = 0
for a in A:
    if dp[a]:
        # print(a, dp[a], math.log2(a), 2**int(math.log2(a) + 1) - a)
        dp[a] -= 1
        if dp.get(2 ** int(math.log2(a) + 1) - a, 0) > 0:
            dp[2 ** int(math.log2(a) + 1) - a] -= 1
            ans += 1
print(ans)


# C
# def next_S(pre_S, length):
#     if length > len(pre_S):
#         S = pre_S + [1] * (length - len(pre_S))
#     else:
#         S = pre_S[:length]
#         maxs = max(S)
#         if min(S) == maxs:
#             S[-1] += 1
#         else:
#             for i in range(length):
#                 if S[length - i - 1] != maxs:
#                     S[length - i - 1] += 1
#                     break
#     return S
#
# N, As = int(input()), list(map(int, input().split()))
# # S, char_max = [1] * As[1], 1
# # for A in As[1:]:
# #     S = next_S(S, A)
# #     char_max = max(char_max, max(S))
# #     # print(A, S, char_max)
# # print(char_max)
#
# maxA, ans = max(As), 1
# while True:
#     # maxnum = pow(ans, maxA) - 1
#     # for i in range(maxA):
#     #     maxnum += pow(ans, i)
#     # print(maxnum)
#     if pow(ans, maxA) - 1 > N:
#         break
#     ans += 1
# print(ans)
