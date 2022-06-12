import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline().strip

# A
# print('YES') if input() in ('7','5','3') else print('NO')

# B
# S, dif = input(), 1000
# for i in range(len(S) - 2):
#     dif = min(dif, abs(int(S[i:i+3] - 753)))
# print(dif)

# C
# def num753(num, keta):
#     if len(num) >= keta:
#         yield num
#     else:
#         for n in ('3', '5', '7'):
#             for nu in num753(num + n, keta):
#                 yield nu
#
# N, ans = input(), 0
# for i in range(3, len(N)+1):
#     for num in num753('', i):
#         if '3' in num and '5' in num and '7' in num:
#             if int(num) <= int(N):
#                 ans += 1
# print(ans)

# D
