def get_sum (N):
    a = 0
    for i in range(0, N + 1):
        a += i
    return a

print(get_sum(5))