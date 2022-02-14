

# BFS traversal for graphs and trees

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = list()
queue = list()
def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0)
        print(s, end=' ')
        for ne in graph:
            if ne not in visited:
                visited.append(ne)
                queue.append(ne)

# print(bfs(visited, graph, 'A'))
    





class Graph:
    def __init__(self, edges, n):
        self.adjust = [[] for _ in range(n)]

        for (src, dist) in edges:
            self.adjust[src] = self.adjust[dist]
            self.adjust[dist] = self.adjust[src]

  

def bfs(graph, v, visited):
    q = list()
    visited[v] = True
    q.append(v)
    while q:
        v = q.pop(0) 
        print(v, end=' ')

        for u in graph.adjust[v]:
            if not visited[u]:
                visited[u] = True
                q.append(u)

edges = [
    (1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (5, 9),
    (5, 10), (4, 7), (4, 8), (7, 11), (7, 12)
]

n = 15

graph = Graph(edges, n)
visited = [False] * n

for i in range(n):
    if not visited[i]: 
        bfs(graph, i, visited)