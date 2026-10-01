def dfs(graph, node, visited):
    print(node, end=" ")
    visited.append(node)

    for n in graph[node]:
        if n not in visited:
            dfs(graph, n, visited)

n = int(input("Enter number of vertices: "))
graph = {}

for i in range(n):
    graph[i] = list(map(int, input(f"Enter neighbours of {i}: ").split()))

start = int(input("Enter starting vertex: "))

print("DFS:", end=" ")
dfs(graph, start, [])
