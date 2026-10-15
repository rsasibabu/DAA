n = int(input("Enter vertices: "))
g = [list(map(int, input().split())) for _ in range(n)]
v = [False] * n
v[0] = True
cost = 0

for _ in range(n - 1):
    m = float('inf')
    for i in range(n):
        for j in range(n):
            if v[i] and not v[j] and 0 < g[i][j] < m:
                m, u, w = g[i][j], i, j

    v[w] = True
    cost += m
    print(u, "-", w, ":", m)

print("Minimum cost:", cost)
