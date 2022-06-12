import sys

sys.stdin = open("input.txt")


def input():
    return sys.stdin.readline().strip()


# n = int(input())
# [int(i) for i in input().split()]


# A
# a, b = [int(i) for i in input().split()]
# if b % a == 0:
#     print(a + b)
# else:
#     print(b - a)


# B
# n, m = [int(i) for i in input().split()]
# li = [0] * m
# for i in range(n):
#     a = [int(i) for i in input().split()][1:]
#     for j in a:
#         li[j-1] += 1
# li = [1 for l in li if l == n]
# print(len(li))


# C
# n = int(input())
# As = [int(i) for i in input().split()]
#
# while True:
#     m = min(As)
#     idx = As.index(m)
#     As = [a if i == idx else a % m for i, a in enumerate(As)]
#     As = [a for a in As if a > 0]
#     print(idx, m, As)
#     if len(As) == 1:
#         break
# print(As[0])


# D
match = [None, 2, 5, 5, 4, 5, 6, 3, 7, 6]
number = [None, None, [1], [7], [4], [5, 3, 2], [9, 6], [8]]
n, m = [int(i) for i in input().split()]
As = sorted([int(i) for i in input().split()], reverse=True)
need = [match[a] for a in As]
print(As, need)

need_sort = sorted(need)

min_match = min(need)
min_idx = need.index(min_match)
min_number = As[min_idx]


if n % need_sort[0] == 0:
    min_m = need_sort[0]
    print(str(number[min_m]) * int(n / min_m))
