def factorize(n):
    b = 2
    fct = set()
    while b * b <= n:
        while n % b == 0:
            n //= b
            fct.add(b)
        b = b + 1
    if n > 1:
        fct.add(n)
    return fct


print(factorize(7))
print(factorize(14))
print(factorize(58))
