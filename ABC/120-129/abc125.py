import sys

sys.stdin = open("input.txt")

# A
# a,b,t = [int(i) for i in input().split()]
# print(int(((t+0.5) // a ) * b))

# B
# n = int(input())
# vs = [int(i) for i in input().split()]
# cs = [int(i) for i in input().split()]
# tmp = [v - c for v, c in zip(vs, cs)]
# print(sum(t for t in tmp if t > 0))


# C
# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a
#
# n = int(input())
# a = [int(i) for i in input().split()]
# l, r = [0], [0]
# for i in range(n):
#     l = l + [gcd(l[i], a[i])]
#     r = [gcd(r[0], a[n - 1 - i])] + r
# # print(l, r)
# ans = 0
# for i in range(n):
#     ans = max(ans, gcd(l[i], r[i + 1]))
# print(ans)

N = int(input())
A_list = list(map(int, input().split()))


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors


divisors = list(set(make_divisors(A_list[0]) + make_divisors(A_list[1])))
print(make_divisors(A_list[0]))
print(divisors)
divisors.sort(reverse=True)
print(divisors)

counter = 0
for divisor in divisors:
    for A in A_list:
        if A % divisor != 0:
            counter += 1
        if counter > 1:
            break
    if counter <= 1:
        print(divisor)
        break
    else:
        counter = 0

# D
# n = int(input())
# As = [int(i) for i in input().split()]
# absl = [abs(a) for a in As]
# neg = sum(1 for a in As if a < 0)
# if neg % 2 == 0:
#     print(sum(absl))
# else:
#     print(sum(absl) - min(absl) * 2)
