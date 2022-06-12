import sys

sys.stdin = open("input.txt")


def input():
    return sys.stdin.readline().strip()


# A
# H, W = map(int, input().split())
# h, w = map(int, input().split())
# print((H - h) * (W -  w))


# B
# n, m, c = [int(i) for i in input().split()]
# Bs = [int(i) for i in input().split()]
# ans = 0
# for i in range(n):
#     As = [int(i) for i in input().split()]
#     mul = sum(a * b for a, b in zip(As, Bs))
#     ans += 1 if mul + c > 0 else 0
# print(ans)


# C
# n, m = [int(i) for i in input().split()]
# ABs = sorted([[int(i) for i in input().split()] for _ in range(n)])
# ans, num = 0, 0
# for a, b in ABs:
#     ans += a * min(b, m - num)
#     num += min(b, m - num)
#     if num == m:
#         break
# print(ans)


# D
def f(x):
    if x % 4 == 0:
        return x
    elif x % 4 == 1:
        return 1
    elif x % 4 == 2:
        return x + 1
    else:
        return 0


a, b = map(int, input().split())
print(f(a - 1) ^ f(b))
