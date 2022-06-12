import sys

sys.stdin = open("input.txt")


def input():
    return sys.stdin.readline().strip()


# n = int(input())
# [int(i) for i in input().split()]

# A
# s = int(''.join(input().split('/')))
# if s <= 20190430:
#     print('Heisei')
# else:
#     print('TBD')


# B
# n = int(input())
# ans = 0
# for i in range(n):
#     x, u = input().split()
#     ans += float(x) * (380000 if u == 'BTC' else 1)
# print(ans)


# C
# n, a, b, c = [int(i) for i in input().split()]
# ls = [int(input()) for i in range(n)]
# abc = [a, b, c]
# ans = 0
# for x in abc[:]:
#     if x in ls:
#         abc.remove(x)
#         ls.remove(x)
#
# if not len(abc):
#     print(ans)

N, A, B, C = map(int, input().split())
l = [int(input()) for i in range(N)]


def dfs(cur, a, b, c):
    # cur本目の竹
    # どれにも1本以上の材料あれば，延長/短縮魔法で解決
    # 1本目の材料では合成の必要がないので-10*3
    if cur == N:
        return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a, b, c) > 0 else 1e9
    ret0 = dfs(cur + 1, a, b, c)  # 使わない
    ret1 = dfs(cur + 1, a + l[cur], b, c) + 10  # Aの材料
    ret2 = dfs(cur + 1, a, b + l[cur], c) + 10  # Bの材料
    ret3 = dfs(cur + 1, a, b, c + l[cur]) + 10  # Cの材料
    return min(ret0, ret1, ret2, ret3)


print(dfs(0, 0, 0, 0))


# D
# from bisect import bisect_left
# INF = 1e10
# a, b, q = [int(i) for i in input().split()]
# ss = [-INF] + [int(input()) for i in range(a)] + [INF]
# ts = [-INF] + [int(input()) for i in range(b)] + [INF]
# xs = [int(input()) for i in range(q)]
# # print(ss, ts, xs)
# for x in xs:
#     idx_s = bisect_left(ss, x)
#     idx_t = bisect_left(ts, x)
#     ans = INF
#     for s in [ss[idx_s - 1], ss[idx_s]]:
#         for t in [ts[idx_t - 1], ts[idx_t]]:
#             a1 = abs(x - s) + abs(s - t)
#             a2 = abs(x - t) + abs(t - s)
#             ans = min(ans, a1, a2)
#     print(ans)
