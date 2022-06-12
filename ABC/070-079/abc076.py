# unfin

# (A)
# r = int(input())
# g = int(input())
# print(r + (g - r) * 2)

# (B)
# n = int(input())
# k = int(input())
# ans = 1
# for _ in range(n):
#     ans += min(ans, k)
# print(ans)

# (C)
s = input()
t = input()
if len(s) < len(t):
    print("UNRESTORABLE")
else:
    for i in range(len(s) - len(t) + 1):
        if all((s[i + j] == "?" or s[i + j] == t[j]) for j in range(len(t))):
            s = s[:i] + t + s[i + len(t) :]
            break
    if t not in s:
        print("UNRESTORABLE")
    else:
        print(s.replace("?", "a"))


# (D)
