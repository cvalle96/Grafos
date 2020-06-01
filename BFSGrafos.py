import collections

def BFS(G, s):
    vis, Q = {s}, collections.deque([s])
    print("\n<<   ANCHURA   >> nodo de salida -->", s , end=" ")
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if v not in vis:
                vis.add(v)
                Q.append(v)
                print(v, end = " ")


G = {"0": ["1", "3"],
     "1": ["0", "2", "4"],
     "2": ["0", "1", "5"],
     "3": ["0", "4", "5"],
     "4": ["1", "3", "5"],
     "5": ["2", "3"]}

s = '5'

print(BFS(G, s))