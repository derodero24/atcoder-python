import io
import sys

# print(['No', 'Yes'][int(input()) >= 30])
# int(input())
# map(int, input().split())
# [int(i) for i in input().split()]


def main():
    # A
    # print('Yes' if int(input()) >= 30 else 'No')
    # print(['No', 'Yes'][int(input()) >= 30])

    # B
    # from math import sqrt
    # n, d = map(int, input().split())
    # ans = 0
    # for i in range(n):
    #     x, y = map(int, input().split())
    #     if sqrt(x**2 + y**2) <= d:
    #         ans += 1
    # print(ans)

    # C
    # k = int(input())
    # a = 0
    # for i in range(k):
    #     a = (a * 10 + 7) % k
    #     if a == 0:
    #         print(i + 1)
    #         break
    # else:
    #     print(-1)

    # D
    # _, c = input(), input()
    # print(c[:c.count('R')].count('W'))


if __name__ == '__main__':
    with open('input.txt') as f:
        inp_list = f.read().split('\n\n')
        # print(inp_list)

    for inp in inp_list:
        sys.stdin = io.StringIO(inp)
        # print('\n>>> ', inp)
        main()
