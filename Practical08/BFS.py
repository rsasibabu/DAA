def bfs(graph, start):
    queue = [start]
    visited = [start]

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for n in graph[node]:
            if n not in visited:
                visited.append(n)
                queue.append(n)

n = int(input("Enter number of vertices: "))
graph = {}

for i in range(n):
    graph[i] = list(map(int, input(f"Enter neighbours of {i}: ").split()))

start = int(input("Enter starting vertex: "))

print("BFS:", end=" ")
bfs(graph, start)
