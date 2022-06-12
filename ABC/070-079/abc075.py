# fin

# (A)
# a,b,c = map(int,input().split())
# print(a if b==c else -a+b+c)

# 方法２
# print(eval(input().replace(' ','^')))

# (B)
# h,w = map(int,input().split())
# s = [input() for i in range(h)]
#
# way = ((1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1))
# ans = [[0 for j in range(w)] for i in range(h)]
#
# for i in range(h):
#     for j in range(w):
#         if s[i][j] == '#':
#             ans[i][j] = '#'
#             continue
#         for k in way:
#             if not (0 <= i+k[0] < h and 0 <= j+k[1] < w): continue
#             if s[i+k[0]][j+k[1]] == '#': ans[i][j] += 1
#
# for i in range(h):
#     print(''.join(map(str,ans[i])))

# (C)
# n, m = map(int,input().split())
# table = [[0 for j in range(n)] for i in range(n)]
# v = []
# for i in range(m):
#     a, b = map(int,input().split())
#     table[a-1][b-1] = table[b-1][a-1] = 1
#     v.append((a-1,b-1))
#
# def check(p):
#     used[p] = 1
#     for i in range(n):
#         if p != i and table[p][i] == 1 and used[i] != 1:
#             check(i)
#
# ans = 0
# for i in range(m):
#     table[v[i][0]][v[i][1]] = table[v[i][1]][v[i][0]] = 0
#     used = [0] * n
#     check(0)
#     if(sum(used) != n): ans += 1
#     table[v[i][0]][v[i][1]] = table[v[i][1]][v[i][0]] = 1
#
# print(ans)

# (D)
n, k = map(int, input().split())
ps = [tuple(map(int, input().split())) for i in range(n)]

sx = sorted(ps, key=lambda x: x[0])  # x座標でソート
nx = list(enumerate(sx))  # 頂点番号を付加
ans = 5e18

for f, (x1, y1) in nx[: n - k + 1]:  # 左辺の頂点
    for e, (x2, y2) in nx[f + k - 1 :]:  # 右辺の頂点
        dx = x2 - x1  # 横
        sy = sorted(y for x, y in sx[f : e + 1])  # 含まれる頂点をy座標でソート
        for y3, y4 in zip(sy, sy[k - 1 :]):  # y3=下辺の頂点，y4=上辺の頂点
            if y3 <= y1 and y4 >= y2:  # 左右辺の頂点を含むこと
                ans = min(ans, dx * (y4 - y3))

print(ans)
