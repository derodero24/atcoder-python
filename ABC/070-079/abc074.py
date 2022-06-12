# fin

# (A)
# print(int(input())**2 - int(input()))

# (B)
# n = int(input())
# k = int(input())
# x = list(map(int, input().split()))
# print(ans([ min( k-x[i], x[i] ) * 2 for i in range(n) ]))

# (C)
# < Method 1 >
# A,B,C,D,E,F = map(int,input().split())
# c_max = 0
# sw_max = 0
# s_max = 0
#
# for a in range(F//100*A+1):
#     for b in range((F-a*A*100)//100*B+1):
#         water = 100*(a*A+b*B)
#         limit = F-water
#         for c in range(limit//C+1):
#             for d in range((limit-c*C)//D+1):
#
#                 sugar = c*C + d*D
#
#                 if water == 0 or sugar == 0:
#                     continue
#                 conc = sugar / (sugar + water)
#                 if sugar/(water//100) <= E and conc > c_max:
#                     c_max = conc
#                     sw_max = sugar + water
#                     s_max = sugar
# if c_max ==0:
#     sw_max = 100*A
#     s_max=0
# print(sw_max,s_max)

# < Method 2 >
# a,b,c,d,e,f = map(int, input().split())
# w = 0
# s = 0
# ratio = 0
#
# for i in range((f // (b*100))+1):
#     for j in range(((f-(i*b*100))//(a*100))+1):
#         if i == 0 and j == 0:
#             continue
#         smax = min(f-(j*a+i*b)*100,(j*a+i*b)*e)
#         sm = 0
#         for k in range((smax//d)+1):
#             sm = max(sm, k*d+c*((smax-(k*d))//c))
#         if ratio <= sm/((j*a+i*b)*100+sm):
#             ratio = sm/((j*a+i*b)*100+sm)
#             w = (j*a+i*b)*100
#             s = sm
#
# print("%i %i" %(w+s,s))

# (D)
# import numpy as np
# N = int(input())
# A = [np.array(input().split(), dtype=np.int64) for _ in [0]*N]
# inf = 10**10
# for i in range(N):
#     A[i][i] = inf
#
# result = 0
# for i in range(N-1):
#     for j, d1 in enumerate(A[i][i+1:], start=i+1):
#         d2 = np.min(A[i]+A[j])
#         if d1 >= d2:
#             if d1 > d2:
#                 print(-1)
#                 exit()
#         else:
#             result += d1
# print(result)

n = int(input())
a = [list(map(int, input().split())) for i in [None] * n]

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        found = True
        for k in range(n):
            if k == i or k == j:
                continue
            compound = a[i][k] + a[k][j]
            if a[i][j] == compound:
                found = False
                continue
            if a[i][j] > compound:
                print(-1)
                exit()
        if found:
            ans += a[i][j]

print(ans)
