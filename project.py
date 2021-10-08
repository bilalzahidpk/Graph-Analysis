#from distutils.version import LooseVersion
import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.approximation.dominating_set import min_weighted_dominating_set
import re
import Prims
import Kruskal 
import djikstra
import BellmanFord
pos=[]

coordsx=[]

coordsy=[]



Edges=[]
EdgeWeights=[]
dump=[]
f= open('input100.txt','r')


for x in f.readlines():
    dump.append(x)

dump.pop(0)
dump.pop(0)

NumOfNodes=int(dump[0])

dump.pop(0)

dump.pop(0)


for x in range(NumOfNodes):
 coordsx.append(dump[x][2:10])
 

for x in range(NumOfNodes):
 coordsy.append(dump[x][11:19])


for x in range(NumOfNodes):
 pos.append((float(coordsx[x]),float(coordsy[x])))

for x in range(NumOfNodes+1):
 dump.pop(0)

Dig=nx.DiGraph()




a=[]
for x in range(len(dump)):
   a.append(dump[x].replace("155200000.000000",''))   



for x in range(len(a)):
 Edges.append(re.findall(r'\b[0-9][0-9]?\b',a[x]))  




SP=Edges.pop()
Edges.pop()



for x in range(len(a)):
 EdgeWeights.append(re.findall(r'\b\d*.000000\b',a[x]))


EdgeWeights.pop()
EdgeWeights.pop()
  





diadjlist=[]
adjlist=[]
for x in range(NumOfNodes):
    diadjlist.append([])
    adjlist.append([])
    for y in range(NumOfNodes):
        diadjlist[x].append(0)
        adjlist[x].append(0)
    

Sources=[]

for x in range(len(Edges)):
    Sources.append(int(Edges[x][0]))
    Edges[x].pop(0)


for x in range(len(Sources)):
    for y in range(len(Edges[x])):
       if diadjlist[int(Sources[x])][int(Edges[x][y])]==0 or  diadjlist[int(Sources[x])][int(Edges[x][y])]>float(EdgeWeights[x][y]):  
        diadjlist[int(Sources[x])][int(Edges[x][y])]=float(EdgeWeights[x][y])
       if adjlist[int(Sources[x])][int(Edges[x][y])]==0 or adjlist[int(Sources[x])][int(Edges[x][y])]>float(EdgeWeights[x][y]): 
        adjlist[int(Sources[x])][int(Edges[x][y])]=float(EdgeWeights[x][y])
        adjlist[int(Edges[x][y])][int(Sources[x])]=float(EdgeWeights[x][y])
       
def edgescost(E):
    sum=0
    for(u,v) in E:
        sum=sum+diadjlist[u][v]
    return sum




EdgeList=[]

weights=[]

for x in range(len(Sources)):
 for y in range(len(Edges[x])):
      if int(Sources[x])!=int(Edges[x][y]) and EdgeList.count((int(Sources[x]),int(Edges[x][y])))==0:
         EdgeList.append(((int(Sources[x])),int(Edges[x][y])))
         

unvisited=[]
visited=[]


G=nx.Graph()
G.add_edges_from(EdgeList)
nx.draw_networkx(G,pos,True,True)
print("BellmonFord:{}".format(BellmanFord.bellman(diadjlist,6,EdgeList)[2]))
print("Kruskal: {}".format(edgescost(Kruskal.kruskal(adjlist,NumOfNodes))))

print("Prims: {}".format(edgescost(Prims.prim(adjlist,NumOfNodes))))

print("Average Clustering: {}".format(nx.average_clustering(G)))

print("Dijkstra: {}".format(nx.dijkstra_path_length(G,5,2)))


plt.show()