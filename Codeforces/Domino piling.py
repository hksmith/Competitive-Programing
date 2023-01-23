def ans(a, b):
    c = a * b
    return (int(c / 2))
M, N = input().split()
res = ans(int(M), int(N))
print(res)