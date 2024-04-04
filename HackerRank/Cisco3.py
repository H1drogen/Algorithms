
def sExpression(nodes):
    tree = {}
    nodes = nodes.split(' ')
    for node in nodes:
        parent = node[0]
        if parent not in tree:
            tree[parent] = []
        if len(tree[parent]) >= 2:
            return 'E1'
        for child in tree[parent]:
            if child == node[1]:
                return 'E2'
        if node[1] in tree:
            return 'E3'
        tree[parent].append(node[1])

    def dfs(node):
        if node not in tree:
            return node
        children = ','.join(dfs(child) for child in sorted(tree[node]))
        return f'{node}({children})'

    root = nodes[0][0]
    return dfs(root)



def sExpression2(nodes):
    graph = {}
    for node in nodes:
        if node[0] not in graph:
            graph[node[0]] = []
        graph[node[0]].append(node[1])

    def dfs(node):
        if node not in graph:
            return node
        children = ','.join(dfs(child) for child in graph[node])
        return f'{node}({children})'

    return dfs(nodes[0][0])

print(sExpression('(A,B) (A,C) (B,D) (B,E)'))