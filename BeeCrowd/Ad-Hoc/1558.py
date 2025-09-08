N = 10000

sum_of_squares = [0] * (N + 1)
for i in range(int(N**0.5) + 1):
    for j in range(int(N**0.5) + 1):
        s = i * i + j * j
        if s <= N:
            sum_of_squares[s] = 1

try:
    while True:
        m = int(input())
        if 0 <= m <= N and sum_of_squares[m] == 1:
            print("YES")
        else:
            print("NO")
except EOFError:
    pass
