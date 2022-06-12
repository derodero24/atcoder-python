import io
import sys

# print(['No', 'Yes'][int(input()) > 30])
# int(input())
# map(int, input().split())
# [int(i) for i in input().split()]
# [input() for _ in range(n)]


def main():
    # A
    # print(max(len(s) for s in input().split('S')))

    # B
    # from itertools import combinations
    # _, l = input(), sorted(int(i) for i in input().split())
    # if len(l) < 3:
    #     print(0)
    # else:
    #     ans = 0
    #     for v in combinations(l, 3):
    #         if v[0] + v[1] > v[2] and len(set(v)) == 3:
    #             ans += 1
    #     print(ans)

    # C
    # x, k, d = map(int, input().split())
    # x = abs(x)
    # if d * k < abs(x):
    #     ans = abs(x - d * k)
    # elif (k - (x // d)) % 2 == 0:
    #     ans = x % d
    # else:
    #     ans = abs(x % d - d)
    # print(ans)

    # D
    n, k = map(int, input().split())
    cs = [int(i) for i in input().split()]
    ps = [int(i) for i in input().split()]
    # print(n, k, ps, cs)

    ans = -float("inf")
    done = []

    if max(ps) <= 0:
        ans = max(ps)

    else:
        for start in range(1, n + 1):  # 最初の場所
            # 終わってるやつ
            if start in done:
                continue

            now = start
            flag = True
            points = []

            while now != start or flag:
                done.append(now)
                flag = False
                now = cs[now - 1]
                points += [ps[now - 1]]

            if max(points) <= 0:
                ans = max(ans, max(points))

            else:
                len_p = len(points)
                x, y = k // len_p, k % len_p
                # print('x, y', x, y)
                p_sum = sum(points) if sum(points) > 0 else 0

                for i in range(len_p):
                    pp = (points + points)[i : i + len_p]

                    for j in range(y + 1):
                        tmp_ans = p_sum * x + sum(pp[:j])
                        ans = max(ans, tmp_ans)
                    # print(ans, tmp_ans)

                # print(start, points, ans)

    print(ans)


if __name__ == "__main__":
    with open("input.txt") as f:
        inp_list = f.read().split("\n\n")
        # print(inp_list)

    for inp in inp_list:
        sys.stdin = io.StringIO(inp)
        # print('\n>>> ', inp)
        main()
