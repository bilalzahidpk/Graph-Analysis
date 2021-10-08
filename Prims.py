import sys


def prim(G,nodes):
    # initialize the MST and the set X
    MST = set()
    X = set()

    # select an arbitrary vertex to begin with
    X.add(0)
    while len(X) != nodes:
        crossing = set()
        # for each element x in X, add the edge (x, k) to crossing if
        # k is not in X
        for x in X:
            for k in range(nodes):
                if k not in X and G[x][k] != 0:
                    crossing.add((x, k))
        # find the edge with the smallest weight in crossing
        edge = sorted(crossing, key=lambda e:G[e[0]][e[1]])[0]
        # add this edge to MST
        MST.add(edge)
        # add the new vertex to X
        X.add(edge[1])
    return MST