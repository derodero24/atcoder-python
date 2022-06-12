import io
import sys
from itertools import product

# print(['No', 'Yes'][int(input()) > 30])
# int(input())
# map(int, input().split())
# [int(i) for i in input().split()]
# [input() for _ in range(n)]


def main():
    # A
    # from math import ceil
    # n,x,t =[int(i) for i in input().split()]
    # print(ceil(n/x) * t)
    # B
    # total = 0
    # for c in input():
    #     total += int(c)
    # print(['No', 'Yes'][total % 9 == 0])

    # C
    # n = int(input())
    # As = [int(i) for i in input().split()]
    # maxs = [0]
    # for a in As:
    #     maxs.append(max(a, maxs[-1]))
    # maxs = maxs[1:]
    # print(sum(m-a for a, m in zip(As, maxs)))

    # D
INF = float('inf')

H, W = map(int, input().split())
ch, cw = [int(i) - 1 for i in input().split()]
dh, dw = [int(i) - 1 for i in input().split()]
S = [input() for i in range(H)]
# print(S)

B = [[INF for w in range(W)] for h in range(H)]
B[ch][cw] = 0
# print(B)


def get_B(h, w):
    if not ((0 <= h < H) and (0 <= w < W)):
        return INF
    else:
        return B[h][w]


flag = True
while flag:
    flag = False

    for h, w in product(range(H), range(W)):
        if S[h][w] == '#':
            continue

        # 横
        min_v = min(get_B(h - 1, w),
                    get_B(h + 1, w),
                    get_B(h, w - 1),
                    get_B(h, w + 1))

        # ワープ
        for i, j in product(range(5), repeat=2):
            if not ((0 <= h - i + 2 < H) and (0 <= w - j + 2 < W)):
                continue
            min_v = min(min_v,
                        B[h - i + 2][w - j + 2] + 1)

        if B[h][w] > min_v:
            B[h][w] = min_v
            flag = True
            # for b in B:
            #     print(b)
            # print()

print(B[dh][dw] if B[dh][dw] != INF else -1)
# for b in B:
#     print(b)
# print()


if __name__ == '__main__':
    with open('input.txt') as f:
        inp_list = f.read().split('\n\n')
        # print(inp_list)

    for inp in inp_list:
        sys.stdin = io.StringIO(inp)
        # print('\n>>> ', inp)
        main()
