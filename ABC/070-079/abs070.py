# fin

# (A)
# n = input()
# if n == n[::-1]:
#     print("Yes")
# else :
#     print("No")

# (B)
# a, b, c, d = map(int, input().split())
# r = set(range(a,b)) & set(range(c,d))
# print(len(r))

# (C)
# def gcd(a,b):
# #     if b == 0: return a
# #     if a < b: a, b = b, a
# #     if a % b == 0: return b
#     while b:
#         a, b = b, a % b
#     return a
#
# def lcd(a,b):
#     return a * b // gcd(a,b)
#
# n = int(input())
# t = [int(input()) for i in range(n)]
# ans = 1
# for i in t:
#     ans = lcd(ans, i)
# print(int(ans))

# (D)
from sys import stdin

line = stdin.readline


def dfs(k, path, n):
    """連結情報path,頂点の個数Nが与えられたとき
    頂点Kから各頂点までの距離をlistで返す"""
    from collections import deque  # deque(),popleft()

    dist = [-1] * n
    dist[k] = 0
    que = deque([])
    que.append(k)
    while que:
        label = que.popleft()
        for i, c in path[label]:  # 頂点labelと連結している頂点iと距離c
            if dist[i] == -1:
                dist[i] = dist[label] + c
                que += [i]  # 次に調べる頂点に
    return dist


n = int(line())
path = [[] for i in range(n)]
for i in range(n - 1):
    a, b, c = map(int, input().split())
    path[a - 1] += [(b - 1, c)]
    path[b - 1] += [(a - 1, c)]

q, k = map(int, input().split())
xy = [list(map(int, input().split())) for i in range(q)]
dis = dfs(k - 1, path, n)
for i in range(q):
    print(dis[xy[i][0] - 1] + dis[xy[i][1] - 1])
