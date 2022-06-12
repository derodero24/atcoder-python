import sys

sys.stdin = open("input.txt")

# (A)
# print(input().count('1'))

# (B)
# n = input()
# A = list(map(int, input().split()))
# count = 0
# while all(a % 2 == 0 for a in A):
#     A = [a / 2 for a in A]
#     count += 1
# print(count)

# (C)
N, K = map(int, input().split())
A = list(map(int, input().split()))
print(N, K, A)


# (D)
