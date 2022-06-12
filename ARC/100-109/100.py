import sys

sys.stdin = open("input.txt")


def input():
    return sys.stdin.readline().strip()


# C
# N, As = int(input()), map(int, input().split())
# As = sorted([A - i - 1 for i, A in enumerate(As)])
# b = As[N // 2]
# print(sum(map(lambda A: abs(A - b), As)))

# D
N, As = int(input()), map(int, input().split())

# E

# F
