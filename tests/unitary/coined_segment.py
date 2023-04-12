import numpy as np
from sys import path as sys_path
sys_path.append('../')
sys_path.append('../../')
import qwalk.coined as hpcoined
import unittest
from test_constants import *

class TestCoinedSegment(unittest.TestCase):

    @unittest.skipIf(not TEST_NONHPC, 'Skipping nonhpc tests.')
    def test_persistent_shift_state_transfer(self):
        # initial state in leftmost vertex
        # final state in rightmost vertex

        num_vert = 10
        seg = hpcoined.Segment(num_vert)

        init_cond = seg.state([(1, 0, 0)])
        S = seg.persistent_shift_operator()
        final_state = seg.simulate_walk(S, init_cond, num_vert - 1)
        final_state = final_state[0]

        self.assertTrue(
            final_state[-1] == 1 and np.all(final_state[:-1] == 0)
        )
