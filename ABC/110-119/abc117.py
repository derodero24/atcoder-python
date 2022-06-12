import sys

sys.stdin = open("input.txt")


def input():
    return sys.stdin.readline().strip()


# n = int(input())
# [int(i) for i in input().split()]

# A
# t, x = [int(i) for i in input().split()]
# print(t / x)


# B
# n = int(input())
# ls = sorted([int(i) for i in input().split()])
# if ls[-1] < sum(ls[:-1]):
#     print('Yes')
# else:
#     print('No')


# C
# n, m = [int(i) for i in input().split()]
# xs = sorted([int(i) for i in input().split()])
# li = sorted([xs[i+1] - xs[i] for i in range(m-1)])
# if n >= m:
#     print(0)
# elif n == 1:
#     print(sum(li))
# else:
#     print(sum(li[:-n+1]))


# D
n, k = [int(i) for i in input().split()]
As = [int(i) for i in input().split()]


def func(x):
    return sum(a ^ x for a in As)


bs = ["{:050b}".format(a)[::-1] for a in As]
# print(bs)
strk = "{:b}".format(k)
ans = ["0"] * len(strk)
# print(strk, ans)
for i in range(len(strk)):
    one = len([True for b in bs if b[len(strk) - 1 - i] == "1"])
    zero = len([True for b in bs if b[len(strk) - 1 - i] == "0"])
    # print(zero, one)
    tmp = ans[:]
    if zero >= one:
        tmp[i] = "1"
    if k >= int("".join(tmp), 2):
        ans = tmp
    # print('ans', ans)

print(func(int("".join(ans), 2)))
