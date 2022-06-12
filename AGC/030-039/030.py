import sys
sys.stdin = open('input.txt')
def input(): return sys.stdin.readline().strip()

# A
# a, b, c = map(int, input().split())
# if a + b > c - 2:
#     print(b + c)
# else:
#     print(b + (a + b + 1))

# B
l, n = map(int, input().split())
xs = [int(input()) for _ in range(n)]
ans, now, fin = 0, 0, False
i, j = 0, n - 1
while i <= j:
    root1 = xs[i] - now if now < xs[i] else xs[i] + (l - now)
    root2 = now - xs[j] if now > xs[j] else now + (l - xs[j])
    ans += max(root1, root2)
    if root1 > root2:
        now = xs[i]
        i += 1
    else:
        now = xs[j]
        j -= 1
print(ans)
