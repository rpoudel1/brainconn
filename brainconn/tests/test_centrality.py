# emacs: -*- mode: python-mode; py-indent-offset: 4; tab-width: 4 -*-
# ex: set sts=4 ts=4 sw=4 et:
import os.path as op

import numpy as np
from brainconn import centrality
from brainconn.tests.utils import (load_sample, MAT_DIR)


def test_edge_betweenness_wei():
    n = 200
    data = np.random.random((n, n))
    data -= np.eye(n)
    edge_betw, node_betw = centrality.edge_betweenness_wei(data)
    assert edge_betw.shape == data.shape
    assert node_betw.shape == data.shape[:1]


def test_pc():
    x = load_sample(thres=.4)
    # ci,q = bc.modularity_und(x)
    ci = np.load(op.join(MAT_DIR, 'sample_partition.npy'))

    pc = np.load(op.join(MAT_DIR, 'sample_pc.npy'))

    pc_ = centrality.participation_coef(x, ci)
    print(list(zip(pc, pc_)))

    assert np.allclose(pc, pc_, atol=0.02)


def test_participation():
    W = np.eye(3)
    ci = np.array([1, 1, 2])

    assert np.allclose(centrality.participation_coef(W, ci), [0, 0, 0])
    assert np.allclose(centrality.participation_coef_sign(W, ci)[0],
                       [0, 0, 0])

    W = np.ones((3, 3))
    assert np.allclose(centrality.participation_coef(W, ci), [
        0.44444444, 0.44444444, 0.44444444])
    assert np.allclose(centrality.participation_coef_sign(W, ci)[0], [
        0.44444444, 0.44444444, 0.44444444])

    W = np.eye(3)
    W[0, 1] = 1
    W[0, 2] = 1
    assert np.allclose(centrality.participation_coef(W, ci),
                       [0.44444444, 0, 0])
    assert np.allclose(centrality.participation_coef_sign(W, ci)[0],
                       [0.44444444, 0, 0])

    W = np.eye(3)
    W[0, 1] = -1
    W[0, 2] = -1
    W[1, 2] = 1
    assert np.allclose(centrality.participation_coef_sign(W, ci)[0],
                       [0., 0.5, 0.])


def test_gateway():
    x = load_sample(thres=.1)
    ci = np.load(op.join(MAT_DIR, 'sample_partition.npy'))

    g_pos, _ = centrality.gateway_coef_sign(x, ci)

    print(np.sum(g_pos), 43.4382)
    assert np.allclose(np.sum(g_pos), 43.4382, atol=.001)

    gpb, _ = centrality.gateway_coef_sign(x, ci, centrality_type='betweenness')

    print(np.sum(gpb), 43.4026)
    assert np.allclose(np.sum(gpb), 43.4026, atol=.001)


def test_zi():
    x = load_sample(thres=.4)
    ci = np.load(op.join(MAT_DIR, 'sample_partition.npy'))

    zi = np.load(op.join(MAT_DIR, 'sample_zi.npy'))

    zi_ = centrality.module_degree_zscore(x, ci)
    print(list(zip(zi, zi_)))

    assert np.allclose(zi, zi_, atol=0.05)
    # this function does the same operations but varies by a modest quantity
    # because of the matlab and numpy differences in population versus
    # sample standard deviation. i tend to think that using the population
    # estimator is acceptable in this case so i will allow the higher
    # tolerance.

# TODO this test does not give the same results, why not


def test_shannon_entropy():
    x = load_sample(thres=0.4)
    ci = np.load(op.join(MAT_DIR, 'sample_partition.npy'))
    hpos, _ = centrality.diversity_coef_sign(x, ci)
    print(np.sum(hpos))
    print(hpos[-1])
    assert np.allclose(np.sum(hpos), 102.6402, atol=.01)
