n, m, a = map(int, input().split())

theatreSquare = n * m
flagstones = a * a

print(theatreSquare // flagstones * 2)