n = int(input("Enter vertices: "))
m = int(input("Enter edges: "))
e = [list(map(int, input().split())) for _ in range(m)]
e.sort()

p = list(range(n))

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

cost = 0
count = 0

for w, u, v in e:
    a, b = find(u), find(v)
    if a != b:
        p[a] = b
        cost += w
        count += 1
        print(u, "-", v, ":", w)
        if count == n - 1:
            break

print("Minimum cost:" if count == n - 1 else "MST not possible", cost if count == n - 1 else "")
