import sys

input = sys.stdin.readline

# A
# x, y = map(int, input().split())
# print(x + y//2)


# B
# N = int(input())
# T, A = map(int, input().split())
# Hs = list(map(int, input().split()))
#
# minAH, mini = 10000000, None
# for i in range(N):
#     AH = abs(A - (T - Hs[i] * 0.006))
#     if minAH > AH:
#         minAH = AH
#         mini = i + 1


# C
N, M = map(int, input().split())
inputs, cities = [], [[] for _ in range(N)]
for i in range(M):
    P, Y = map(int, input().split())
    inputs.append((P, Y))
    cities[P - 1].append(Y)

# cities = [sorted(city) for city in cities]
cities = list(map(sorted, cities))

for i in range(M):
    P, Y = inputs[i]
    idx = cities[P - 1].index(Y)
    print("%06d" % P + "%06d" % (idx + 1))


# D
H, W, K = map(int, input().split())
