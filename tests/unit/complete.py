from sys import path as sys_path
sys_path.append('../')
sys_path.append('../../')
from test_constants import *
import unittest
import numpy as np
import hiperwalk as hpw

class TestComplete(unittest.TestCase):
    
    def setUp(self):
        self.n = 50
        self.g = hpw.Complete(self.n)

    def test_adjacency_matrix(self):
        A = np.ones((self.n, self.n)) - np.eye(self.n)
        A2 = self.g.adjacency_matrix()
        self.assertTrue(np.all(A - A2 == 0))

    def test_laplacian_matrix(self):
        L = self.n*np.eye(self.n) - np.ones((self.n, self.n))
        L2 = self.g.laplacian_matrix()
        self.assertTrue(np.all(L - L2 == 0))

    def test_multigraph(self):
        adj = self.g.adjacency_matrix()
        self.assertTrue(id(adj) != id(self.g._adj_matrix))

        adj[0, 1] = 2
        adj[1, 0] = 2
        adj[0, 2] = 3
        adj[2, 0] = 3

        mg = hpw.Multigraph(adj, copy=True)
        self.assertTrue(id(adj) != id(mg._adj_matrix))
        self.assertTrue(id(adj) != id(mg.adjacency_matrix()))
        self.assertTrue(np.sum(adj - mg.adjacency_matrix()) == 0)

        mh = hpw.Complete(self.n, multiedges=adj, copy=True)
        self.assertTrue(isinstance(mh, hpw.Multigraph))
        self.assertTrue(id(adj) != id(mh._adj_matrix))
        self.assertTrue(id(adj) != id(mh.adjacency_matrix()))
        self.assertTrue(np.sum(adj - mh.adjacency_matrix()) == 0)

        d = {(0, 1): 2, (0, 2): 3}
        mh = hpw.Complete(self.n, multiedges=d)
        self.assertTrue(id(adj) != id(mh._adj_matrix))
        self.assertTrue(id(adj) != id(mh.adjacency_matrix()))
        self.assertTrue(np.sum(adj - mh.adjacency_matrix()) == 0)

        mg = hpw.Multigraph(adj, copy=False)
        self.assertTrue(id(adj) == id(mg._adj_matrix))
        self.assertTrue(id(adj) != id(mg.adjacency_matrix()))

        mh = hpw.Complete(self.n, multiedges=adj, copy=False)
        self.assertTrue(id(adj) == id(mh._adj_matrix))
        self.assertTrue(id(adj) != id(mh.adjacency_matrix()))

        self.assertTrue(np.sum(mg._adj_matrix - mh._adj_matrix) == 0)

    def test_weighted_graph(self):
        adj = self.g.adjacency_matrix()
        self.assertTrue(id(adj) != id(self.g._adj_matrix))

        adj = adj.astype(float)
        adj[0, 1] = 0.2
        adj[1, 0] = 0.2
        adj[0, 2] = 0.3
        adj[2, 0] = 0.3

        wg = hpw.WeightedGraph(adj, copy=True)
        self.assertTrue(id(adj) != id(wg._adj_matrix))
        self.assertTrue(id(adj) != id(wg.adjacency_matrix(True)))
        self.assertTrue(id(adj) != id(wg.adjacency_matrix(False)))
        self.assertTrue(np.sum(adj - wg._adj_matrix) == 0)

        wh = hpw.Complete(self.n, weights=adj, copy=True)
        self.assertTrue(isinstance(wh, hpw.WeightedGraph))
        self.assertTrue(id(adj) != id(wh._adj_matrix))
        self.assertTrue(id(adj) != id(wh.adjacency_matrix(True)))
        self.assertTrue(id(adj) != id(wh.adjacency_matrix(False)))
        self.assertTrue(np.sum(adj - wh._adj_matrix) == 0)

        d = {(0, 1): 0.2, (0, 2): 0.3}
        wh = hpw.Complete(self.n, weights=d)
        self.assertTrue(id(adj) != id(wh._adj_matrix))
        self.assertTrue(id(adj) != id(wh.adjacency_matrix()))
        self.assertTrue(np.sum(adj - wh._adj_matrix) == 0)

        wg = hpw.WeightedGraph(adj, copy=False)
        self.assertTrue(id(adj) == id(wg._adj_matrix))
        self.assertTrue(id(adj) != id(wg.adjacency_matrix(True)))
        self.assertTrue(id(adj) == id(wg.adjacency_matrix(False)))

        wh = hpw.Complete(self.n, weights=adj, copy=False)
        self.assertTrue(id(adj) == id(wh._adj_matrix))
        self.assertTrue(id(adj) != id(wh.adjacency_matrix(True)))
        self.assertTrue(id(adj) == id(wh.adjacency_matrix(False)))

        self.assertTrue(np.sum(wg._adj_matrix - wh._adj_matrix) == 0)
