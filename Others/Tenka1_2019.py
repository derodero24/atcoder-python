import sys

sys.stdin = open("input.txt")

# C
N, S = int(input()), input()
for l, s in enumerate(S):
    if s != ".":
        break
else:
    l += 1
for r, s in enumerate(S[::-1]):
    if s != "#":
        break
else:
    r += 1
r = len(S) - r
print(l, r)
print(S[l:r])

w_num = sum(True for s in S[l:r] if s == "#")
# print(w_num,r - l - w_num)
print(min(w_num, r - l - w_num))


# D
# MOD = 998244353
# N = int(input())
# As = [int(input()) for i in range(N)]
# print(N, As)
#
# a = sorted(set(As))
# sum_a = sum(As)
# print(a, sum_a)
#
# for R in range(sum_a // 2):
#     for G in range()

# E
# def factorize(n):
#     b = 2
#     fct = set()
#     while b * b <= n:
#         while n % b == 0:
#             n //= b
#             fct.add(b)
#         b = b + 1
#     if n > 1:
#         fct.add(n)
#     return fct
#
# ans = set()
# for i in range(int(input()) + 1):
#     a = int(input())
#     ans = ans | factorize(abs(a))
#     print(factorize(abs(a)))
#     if
# print(*ans, sep='\n')
# for


# num = [for]
