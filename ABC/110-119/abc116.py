import sys

sys.stdin = open("input.txt")


def input():
    return sys.stdin.readline().strip()


# A
# a, b, c = sorted([int(i) for i in input().split()])
# print(a * b // 2)

# B
# def f(n):
#     return 3 * n + 1 if n % 2 else n / 2
# a = int(input())
# li = set([a])
# ans = 1
# while True:
#     ans += 1
#     a = f(a)
#     if a in li:
#         break
#     else:
#         li.add(a)
# print(ans)

# C
n = int(input())
hs = [int(i) for i in input().split()]
print(n, hs)
ans = 0
up = True
for i in range(n - 1):
    if up and hs[i] > hs[i + 1]:
        up = False
        ans += 1 + hs[i]
    elif not up and hs[i] < hs[i + 1]:
        up = True
    print(ans)
if up:
    ans += 1 + hs[-1]
print(ans)


# D
