def DFS(G, s):
    vis, pila = {s}, [s]
    print(vis)

    print("\n<< PROFUNDIDAD >> nodo de salida -->", s, end=" ")
    while pila:
        flag = 0
        for i in G[pila[-1]]:
            if i not in vis:
                pila.append(i)
                vis.add(i)
                flag = 1
                print(i, end=" ")
                break
        if not flag:
            pila.pop()


G = {"0": ["1", "3"],
     "1": ["0", "2", "4"],
     "2": ["0", "1", "5"],
     "3": ["0", "4", "5"],
     "4": ["1", "3", "5"],
     "5": ["2", "3"]}

s = "5"

print(DFS(G, s))