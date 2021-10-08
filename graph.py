import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()
G.add_node(0)
G.add_node(1)

keywords=[]
keywords.append(0)
keywords.append(1)
a=[]
a.append((7,3))
a.append((4,13))

nx.draw_networkx(G,a,False,True)


plt.show()