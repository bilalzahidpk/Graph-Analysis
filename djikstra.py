import math 


prev=[]
def Dist(Node1,Node2,Adj):
    return Adj[Node1][Node2]

def Djikstra(G,S,E,unvisited,visited):
  
      
    for x in range(len(G)):
        prev.append(None)

    shortestdist=[]
    for x in range(len(G)):
        shortestdist.append(math.inf)

    
     
    
    StartNode=None
    destNode=None
    for x in range(len(G)):
        newNode=x
        unvisited.append(newNode)
        if x==S:
            StartNode=newNode
            shortestdist[StartNode]=0
        if x==destNode:
            destNode=newNode

    while unvisited:
        unv_dist=[]
        for n in unvisited:
            unv_dist.append(shortestdist[n])
        min_dist=min(unv_dist)
        for node in unvisited:
            if shortestdist[node]==min_dist:
                currNode=node
        for node in unvisited:
            if G[currNode][node]!=0:
                neighborNode=node
                temp_dist=Dist(StartNode,currNode,G)+Dist(currNode,neighborNode,G)
                if temp_dist <shortestdist[neighborNode]:
                    shortestdist[neighborNode]=temp_dist
                    prev[neighborNode]=currNode
        unvisited.remove(currNode)
        visited.append(currNode)
    del visited
    del unvisited  
    return findShortestPath(G,S,E)

def findShortestPath(G,S,E):
    
    shortestpath=0
    
    while E!=S:
        shortestpath+=Dist(S,prev[E],G)     
        E=prev[E]
        
    
     



      