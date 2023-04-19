import networkx as nx
import matplotlib.pyplot as plt
import sys
sys.path.append('..')
import qwalk.coined as coined_qw
import plot as hplot

# create random graph and obtain its adjacency matrix
num_vert = 20
edge_prob = 0.25
G = nx.gnp_random_graph(num_vert, edge_prob)
adj = nx.adjacency_matrix(G)
del G

# Quantum Walk preparation and simulation
random = coined_qw.Coined(adj)
# By default uses flip-flop shift operator and Grover coin
random.evolution_operator()
# Initial state at vertex 0 pointing to the first directiong possible
#init_state = random.state([[1, 0, 0]])
#random.set_initial_condition(init_state)
random.initial_condition([[1, 0, 0]])
num_steps = num_vert
random.time((0, num_steps))
states = random.simulate()

# Calculating probabilities and plotting
prob = random.probability_distribution(states)
hplot.plot_probability_distribution(
    prob, plot_type='graph', animate=True, adj_matrix=adj, interval=1000,
    cmap='default', fixed_probabilities=False
)
