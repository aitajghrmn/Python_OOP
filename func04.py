def kvadratlar_listi(n):
    netice = []
    for i in range(1, n+1):
        netice.append(i ** 2)
    return netice

print(kvadratlar_listi(4))