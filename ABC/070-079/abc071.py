# fin
import sys

line = sys.stdin.readline

# (A)
# x,a,b = map(int, line().split())
# print("A" if abs(x-a) < abs(x-b) else "B")

# (B)
# s = input()
# ch = [chr(i) for i in range(ord('a'), ord('z')+1)]
# ss = set()
# for i in range(len(s)): ss.add(s[i])
# tmp = sorted(list(ch ^ ss))
# print(tmp[0] if len(tmp) else "None")

# (C)
# n = int(line())
# a = list(map(int, line().split()))
# h = 0

# ＜方法１＞
# a.sort(reverse=True)
# summ = 0
# for i in range(len(a)):
#     summ += 1
#     if i and a[i] != a[i-1]:
#         summ = 1
#     if summ == 2:
#         if h:
#             print(a[i] * h)
#             sys.exit()
#         else:
#             h = a[i]
#     if summ == 4:
#         print(a[i] * a[i])
#         sys.exit()
# print(0)

# ＜方法２＞
# from collections import Counter
# counter = Counter(a)
# # for word, cnt in counter.most_common():
# #     print(word, cnt)
# for key in sorted(counter.keys(), reverse = True):
#     if h and counter[key] >= 2:
#         print(h * key)
#         sys.exit()
#     if counter[key] >= 4:
#         print(key * key)
#         sys.exit()
#     if counter[key] >= 2:
#         h = key
# print(0)

# (D)
n = int(input())
s1 = input()
s2 = input()

if s1[0] == s2[0]:
    now = True
    ans = 3
    i = 1
else:
    now = False
    ans = 6
    i = 2

while i < n:
    if now:
        ans *= 2
        if s1[i] != s2[i]:
            i += 1
            now = False
    else:
        if s1[i] == s2[i]:
            now = True
        else:
            ans *= 3
            i += 1
    i += 1
print(ans % 1000000007)
