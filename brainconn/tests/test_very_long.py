import numpy as np
import brainconn as bc
from brainconn.tests.utils import (load_sample)


def test_link_communities():
    x = load_sample(thres=0.4)
    seed = 949389104
    M = bc.modularity.link_communities(x)
    assert np.max(M) == 1
