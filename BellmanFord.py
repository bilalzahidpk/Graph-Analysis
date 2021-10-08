import math
def bellman(G,S,E):
 distance=[]
 prev=[]
 for v in range(len(G)):
     distance.append(math.inf)
     prev.append(None)
 distance[S]=0
 for v in range(len(G)):
     for (u,v) in E:
         
         if distance[v]>distance[u]+G[u][v]:
             distance[v]=distance[u]+G[u][v]
             prev[v]=u
 return distance



    



    