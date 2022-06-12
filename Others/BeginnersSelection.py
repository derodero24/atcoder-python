import sys

sys.stdin = open("input.txt")


def input():
    return sys.stdin.readline().strip()


# PracticeA - はじめてのあっとこーだー（Welcome to AtCoder）
# print(int(input())+sum([int(i) for i in input().split()]), input())


# ABC086A - Product
# a, b = map(int, input().split())
# print(['Even', 'Odd'][a * b % 2])


# ABC081A - Placing Marbles
# print(input().count('1'))


# ABC081B - Shift only
# n, As = int(input()), [int(i) for i in input().split()]
# ans = 0
# while all(a % 2 == 0 for a in As):
#     As = [a / 2 for a in As]
#     ans += 1
# print(ans)


# ABC087B - Coins
# a, b, c, x = [int(input()) for i in range(4)]
# ans = 0
# for i in range(a + 1):
#     for j in range(b + 1):
#         for k in range(c + 1):
#             if 500 * i + 100 * j + 50 * k == x:
#                 ans += 1
# print(ans)


# ABC083B - Some Sums
# n, a, b = map(int, input().split())
# ans = 0
# for i in range(1, n + 1):
#     if a <= sum([int(s) for s in str(i)]) <= b:
#         ans += i
# print(ans)


# ABC088B - Card Game for Two
# n, As = input(), sorted([int(i) for i in input().split()], reverse=True)
# print(sum(As[::2]) - sum(As[1::2]))


# ABC085B - Kagami Mochi
# n = int(input())
# print(len(set([input() for i in range(n)])))


# ABC085C - Otoshidama
# n, y = map(int, input().split())
# for i in range(n + 1):
#     for j in range(n + 1 - i):
#         if 10000 * i + 5000 * j + 1000 * (n - i - j) == y:
#             print(i, j, n - i - j)
#             exit()
# print('-1 -1 -1')


# ABC049C - 白昼夢 / Daydream
# s = input().replace('eraser','').replace('erase','').replace('dreamer','').replace('dream','')
# print('NO' if s else 'YES')


# ABC086C - Traveling
# n = int(input())
# lt, lx, ly = 0, 0, 0
# for i in range(n):
#     # print(lt, lx, ly)
#     t, x, y = map(int, input().split())
#     difl = abs(x - lx) + abs(y - ly)
#     dift = t - lt
#     if difl > dift or (dift - difl) % 2:
#         print('No')
#         exit()
#     lt, lx, ly = t, x, y
# print('Yes')
