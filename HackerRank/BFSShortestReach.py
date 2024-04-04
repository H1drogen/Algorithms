
def bfs(n, m, edges, s):
    distances = {}
    ans = []
    for node in range(1, n + 1):
        if s == node:
            continue
        for edge in edges:
            if edge[1] == node:
                distances[node] = 6
                start_node = searchpath(edges, edge[0], node, distances)
                if start_node != s:
                    distances[node] = -1
                break
        if node not in distances.keys():
            distances[node] = -1
    for value in distances.values():
        ans.append(value)
    return ans

def searchpath(edges, newnode, node, distances):
    for edge in edges:
        if edge[1] == newnode:
            distances[node] = distances[newnode] + 6
            return searchpath(edges, edge[0], node, distances)
        else:
            return newnode

# The below code is a solution to the problem of finding the shortest path between nodes in a graph. The code is correct but it is not efficient. The code is not efficient because it uses a recursive function to find the shortest path between nodes. The recursive function is called for each node in the graph, which results in a large number of function calls. This makes the code slow and inefficient. To make the code more efficient, we can use a breadth-first search (BFS) algorithm to find the shortest path between nodes. The BFS algorithm is a graph traversal algorithm that visits all the nodes in a graph in a breadth-first manner. The BFS algorithm is more efficient than the recursive function because it uses a queue to store the nodes that need to be visited. This reduces the number of function calls and makes the code faster. The BFS algorithm is implemented in the following code:
def bfs2(n, m, edges, s):
    graph = {}
    for i in range(1, n + 1):
        graph[i] = []
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    distances = [-1] * (n + 1)
    distances[s] = 0
    queue = [s]
    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[node] + 6
                queue.append(neighbor)
    distances.pop(s)
    distances.pop(0)
    return distances


bfs2(10, 6, [[3, 1], [10, 1], [10,1], [3,1],[1,8],[5,2]], 3)
