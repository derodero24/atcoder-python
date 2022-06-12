import sys

sys.stdin = open("input.txt")


def input():
    return sys.stdin.readline().strip()


# A
# s = ''.join(sorted(input().split()))
# print(['NO', 'YES'][s == '1479'])


# B
# s = input()
# for i in range(7):
#     if s[:i] + s[-7+i:] == 'keyence':
#         print('YES')
#         exit()
# print('NO')


# C
# n = int(input())
# As = [int(i) for i in input().split()]
# Bs = [int(i) for i in input().split()]
# ABs = [a - b for a, b in zip(As, Bs)]
# # print(As, Bs, ABs)
# if sum(As) < sum(Bs):
#     print(-1)
#     exit()
# mABs = [ab for ab in ABs if ab < 0]
# pABs = [ab for ab in ABs if ab > 0]
# ans, t = len(mABs), sum(mABs)
# for ab in sorted(pABs, reverse=True):
#     if t >= 0:
#         break
#     ans += 1
#     t += ab
# print(ans)


# D
N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

A.sort(reverse=True)
B.sort(reverse=True)

MOD = 10**9 + 7
aidx, bidx = 0, 0
ret = 1

for n in range(N * M, 0, -1):
    # 両方みつけた
    if aidx < N and bidx < M and n == A[aidx] and n == B[bidx] and A[aidx] == B[bidx]:
        aidx += 1
        bidx += 1
    # Bの方だけ見つけた
    elif bidx < M and n == B[bidx]:
        ret *= aidx
        bidx += 1
    # Aの方だけ見つけた
    elif aidx < N and n == A[aidx]:
        ret *= bidx
        aidx += 1
    # 両方なかった
    else:
        ret *= aidx * bidx - (N * M - n)
    ret = ret % MOD
print(ret)
