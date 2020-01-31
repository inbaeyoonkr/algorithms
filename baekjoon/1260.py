import sys

n, m, v = map(int, sys.stdin.readline().strip().split())
adj = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    start, end = map(int, sys.stdin.readline().strip().split())
    adj[start].append(end)
    adj[end].append(start)

for e in adj:
    e.sort()


def dfs(start):
    print(start, end=" ")
    visited[start] = True
    for node in adj[start]:
        if not visited[node]:
            dfs(node)


def bfs(start):
    queue = [start]
    visited = [False] * (n+1)

    while queue:
        node = queue.pop(0)
        if not visited[node]:
            visited[node] = True
            print(node, end=" ")
            for pos in adj[node]:
                if not visited[pos]:
                    queue.append(pos)


dfs(v)
print()
bfs(v)
print()
