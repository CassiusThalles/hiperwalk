import hiperwalk as hpw
import numpy as np

num_vert1 = 73
num_vert2 = 42
num_vert = num_vert1 + num_vert2
g = hpw.CompleteBipartite(num_vert1, num_vert2)

qw = hpw.Coined(g, coin='G', marked={'-G': [0]})
time = (int(2*np.sqrt(num_vert)), 1)
states = qw.simulate(time=time,
                     state=qw.uniform_state())

marked_prob = qw.success_probability(states)
hpw.plot_success_probability(time, marked_prob)
