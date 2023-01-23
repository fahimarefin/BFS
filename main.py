import queue
from collections import defaultdict

adj_list = defaultdict(list)
color = {}
parent = {}
dest = {}
queue = queue.Queue()
bfs_traversal = []


def bfs(src, des, node, edge):
    for i in range(1, node + 1):
        color[i] = 0
        parent[i] = -1
        dest[i] = 999999

    color[src] = 1
    dest[src] = 0
    queue.put(src)
    order = 1
    while not queue.empty():
        u = queue.get()
        if u == des:
            break
        
        bfs_traversal.append(u)

        for v in adj_list[u]:

            if not color[v]:
                order = order + 1
                color[v] = order
                dest[v] = dest[u] + 1
                parent[v] = u
                queue.put(v)

    print(dest[des])
    roots = []
    child = des
    while parent[child] != -1:
        step = str(parent[child]) + " " + str(child)
        roots.append(step)
        child = parent[child]
    for i in range(len(roots) - 1, -1, -1):
        print(roots[i])
    for i in range(1, node + 1):
        if parent[i] != -1 or i == src:
            print(color[i])
        else:
            print(-1)


if __name__ == "__main__":
    node, edge = map(int, input().split())
    for i in range(edge):
        u, v = map(int, input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)

    for i in range(edge):
        adj_list[i] = sorted(adj_list[i])

    src, des = map(int, input().split())
    bfs(src, des, node, edge)
