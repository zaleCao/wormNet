import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas
try:
    import pygraphviz
    from networkx.drawing.nx_agraph import graphviz_layout
except ImportError:
    try:
        import pydotplus
        from networkx.drawing.nx_pydot import graphviz_layout
    except ImportError:
        raise ImportError("This example needs Graphviz and either "
                          "PyGraphviz or PyDotPlus")

G = nx.read_graphml("data/c.elegans.herm_pharynx_1.graphml")

plt.figure(figsize=(12,12))
	#pos=nx.spring_layout(G,iterations=100,scale=2.0)
	#n_colors=range(279)
	#e_colors=range(3225)
	pos = graphviz_layout(G, prog='sfdp', args='')
	nx.draw(G,pos, node_color='b',node_size=node_size_map(), width=1, style='dotted', arrows=False)
	#nx.draw_spectral(G)
	plt.savefig("test2.png")
	plt.show()

if __name__ == "__main__":
	# figure setup
	#time iterate through the network
	time_itr()


#assign neurodata type to nodes
def assign_neuro_type():
	colnames = ['NAME', 'GROUP', 'TYPE']
	data = pandas.read_csv('data/neurogroup.csv', names=colnames)
	names = data.NAME.tolist()
	groups = data.GROUP.tolist()
	types = data.TYPE.tolist()
	for n,nbrs in G.adjacency_iter():
		for i in range(len(names)):
			if G.node[n]['cell_name'] == names[i]:
				G.node[n]['cell_type'] = types[i]



#determine if a neuron is excitory in inhibitory
def exin():
	for n,nbrs in G.adjacency_iter():
		data = i[1]
		NT_types = ['Ach', 'DA', 'GABA', '5-HT']
		if G.node[n]['neurotransmitters'] == NT_types[0]:
			G.node[n]['exin'] = 1
		elif G.node[n]['neurotransmitters'] == NT_types[1]:
			G.node[n]['exin'] = 1
		elif G.node[n]['neurotransmitters'] == NT_types[2]:
			G.node[n]['exin'] = -1
		else:
			G.node[n]['exin'] = 0

#initialise all nodes to have the parameter activity

def init_activity():
	init_active_nodes = 0
	for n,nbrs in G.adjacency_iter():
		if len(nbrs) < 10:
			G.node['n']['activity'] = 0
		else:
			G.node['n']['activity'] = 100
			init_active_nodes += 1
		percentage_init_active = init_active_nodes / G.number_of_nodes()
		print(percentage_init_active)

def get_activity():
	activity_array = range(G.number_of_nodes())
	i = 0
	for n,nbrs in G.adjacency_iter():
		size_array[i] = G.node[n]['activity']
		i += 1
	return activity_array



#	G.node['n']['activity']= 0

#randomly initialise nodes

"""
#initialise targeted sensory neurons
for n,nbrs in G.adjacency_iter():
	if len(nbrs) < 10 
		G.node[n]['activity'] = 0
	else
		G.node[n]['activity'] = 100
		init_active_nodes += 1
	percentage_init_active = init_active_nodes / G.number_of_nodes()
	print(percentage_init_active)
"""
#plot graph

def node_size_map():
	size_array = range(G.number_of_nodes())
	i = 0
	for n,nbrs in G.adjacency_iter():
		size_array[i] = G.degree(n) * 5
		i += 1
	return size_array

"""
def node_activity_map():
	activity_array = range(G.number_of_nodes())
	i = 0
	for n,nbrs in G.adjacency_iter():
		size_array[i] = G.degree(n) * 5
		i += 1
	return size_array
"""


#interate over all nodes to propogate neural activity
def single_time_step(node_sizes):
	for n,nbrs in G.adjacency_iter():
		#check if the node is active
		activity_array = range(G.number_of_nodes())
		i = 0
		if G.node[n]['activity'] > 0:
			G.node[n]['activity'] -= 50 
			size_array[i] = G.degree(n) * 5
			i += 1
		else:
			for nbr,eattr in nbrs.items():
				for attr, data in eattr.items():
					if data['synapse_type'] == 'E':
						integral +=  G.node[nbr]['exin'] * G.node[nbr]['activity'] * data['weight']
			if integral > 15:
				G.node[n]['activity'] = 100

	nx.draw(G,pos, node_color=get_activity(), node_size=node_sizes, width=1, style='dotted', arrows=False)
	#nx.draw_spectral(G)
	plt.savefig("img/step.png")
	plt.show()

def time_itr(time):
	init_activity()
	exin()
	assign_neuro_type()
	node_sizes = node_size_map()
	for i in range(time):
		single_time_step(node_sizes)



"""
G=nx.star_graph(4)
pos=nx.spring_layout(G)
colors=range(4)
nx.draw(G,pos,node_color=['#A0CBE2',#EE1BE2',#EE1BE2',#EE1BE2'])


plt.figure(figsize=(12,12))
#pos=nx.spring_layout(G,iterations=100,scale=2.0)
n_colors=range(279)
e_colors=range(3225)
pos = graphviz_layout(G, prog='sfdp', args='')
nx.draw(G,pos,node_color=n_colors, node_cmap=plt.cm.Blues, edge_color=e_colors, edge_cmap=plt.cm.Reds, width=1, style='solid')
#nx.draw_spectral(G)
plt.savefig("test.png")
plt.show()

"""
			
"""
#archive
for n,nbrs in G.adjacency_iter():
	#check if the node is active

	if G.node['n']['activity'] > 0 
		G.node['n']['activity'] -= 1
	else
		for nbr,eattr in nbrs.items():
			for attr, data in eattr.items():
				weight = data['weight']
				synapse = data['synapse_type']
				if weight > 2:
					print ('(%s, %s, %s, %d)' %(n, nbr, synapse, weight))
"""
"""

#test
for n,nbrs in G.adjacency_iter():
	#check if the node is active
	for nbr,eattr in nbrs.items():
			for attr, data in eattr.items():
				weight = data['weight']
				synapse = data['synapse_type']
				if synapse == 'E':
					print ('(%s, %s, %s, %d)' %(n, nbr, synapse, weight))
"""
"""
with open("data/neurogroup.csv") as f:
	c = csv.reader(f, delimiter=' ', skipinitialspace=True)
	for line in c:
		print line[0]
"""
"""
for i in G.nodes(data=True):
	data = i[1]
	NT_types = ['Ach', 'DA', 'GABA', '5-HT']

	if data['neurotransmitters'] == 'Ach':
	 G.
	elif 
"""


