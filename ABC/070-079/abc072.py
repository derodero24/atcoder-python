# fin

# (A)
# x, t = map(int, input().split())
# print(x-t if x>t else 0)

# (B)
# s = input()
# print(s[::2])

# (C)
# n = int(input())
# a = list(map(int, input().split()))
# g = [0] * (max(a) + 3)
# for i in a:
#     g[i] += 1
#     g[i + 1] += 1
#     g[i + 2] += 1
# print(max(g))

# (D)
n = int(input())
p = list(map(int, input().split()))
ans = 0
now = False
for i in range(n):
    if p[i] == i + 1 and not now:
        ans += 1
        now = True
    else:
        now = False
print(ans)
