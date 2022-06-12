# fin

# (A)
# n = input()
# for i in range(len(n)):
#     if n[i] == '9':
#         print("Yes")
#         break
# else:
#     print("No")

# 方法２
# print("Yes" if "9" in input() else "No")

# (B)
# n = int(input())
# ans = 0
# for i in range(n):
#     l, r = map(int, input().split())
#     ans += r - l + 1
# print(ans)

# (C)
# n = int(input())
# dic = {}
# for i in range(n):
#     a = input()
#     if a in dic:
#         del dic[a]
#     else:
#         dic[a] = None
# print(len(dic))

from heapq import heappop, heappush

# (D)
from itertools import permutations


def inpl():
    return tuple(map(int, input().split()))


N, M, R = inpl()
inf = float("inf")
G = {n: {} for n in range(N + 1)}
Des = inpl()

for _ in range(M):
    a, b, c = inpl()
    G[a][b] = c
    G[b][a] = c


def dijkstra(s):
    D = [inf for _ in range(N + 1)]
    D[s] = 0
    HQ = [(0, s)]
    checked = [False for _ in range(N + 1)]
    while HQ:
        c1, a = heappop(HQ)
        if D[a] < c1 or checked[a]:
            continue
        for b, c2 in G[a].items():
            if c1 + c2 < D[b]:
                D[b] = c1 + c2
                heappush(HQ, (D[b], b))
        checked[a] = True
    return D


#     return [D[des] for des in Des]

C = []
for s in range(max(Des) + 1):
    C.append(dijkstra(s))

res = inf
for E in permutations(Des):
    res = min(res, sum([C[E[i]][E[i + 1]] for i in range(len(E) - 1)]))

print(res)
