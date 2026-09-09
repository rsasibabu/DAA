n = int(input("Enter number of matrices: "))

print("Enter dimensions:")
p = list(map(int, input().split()))

m = [[0] * n for _ in range(n)]

for length in range(2, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1
        m[i][j] = float('inf')

        for k in range(i, j):
            cost = (m[i][k] + m[k + 1][j] +
                    p[i] * p[k + 1] * p[j + 1])

            if cost < m[i][j]:
                m[i][j] = cost

print("Minimum number of multiplications:", m[0][n - 1])
