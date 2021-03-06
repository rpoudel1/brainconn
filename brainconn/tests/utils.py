# emacs: -*- mode: python-mode; py-indent-offset: 4; tab-width: 4 -*-
# ex: set sts=4 ts=4 sw=4 et:
import os.path as op
import numpy as np
import brainconn as bc

MAT_DIR = op.join(op.dirname(op.realpath(__file__)), 'data')


def load_sample(thres=1):
    return bc.utils.threshold_proportional(np.load(
        op.join(MAT_DIR, 'sample_data.npy')), thres, copy=False)


def load_signed_sample(thres=1):
    return bc.utils.threshold_proportional(np.around(
        np.load(op.join(MAT_DIR, 'sample_signed.npy')), 8), thres, copy=False)


def load_sparse_sample(thres=.02):
    return load_sample(thres=thres)


def load_binary_sample(thres=.35):
    return bc.utils.binarize(load_sample(thres=thres), copy=False)


def load_directed_sample(thres=1):
    return bc.utils.threshold_proportional(np.load(
        op.join(MAT_DIR, 'sample_directed.npy')), thres, copy=False)


def load_binary_directed_sample(thres=.35):
    return bc.utils.binarize(load_directed_sample(thres=thres))


def load_directed_low_modularity_sample(thres=1):
    return bc.utils.threshold_proportional(np.load(
        op.join(MAT_DIR, 'sample_directed_gc.npy')), thres, copy=False)


def load_binary_directed_low_modularity_sample(thres=.35):
    return bc.utils.binarize(load_directed_low_modularity_sample(thres=thres))

# unimplemented samples


def load_binary_sparse_sample(thres=.35):
    raise NotImplementedError()


def load_binary_directed_sparse_sample(thres=.02):
    raise NotImplementedError()


def load_directed_sparse_sample(thres=.02):
    raise NotImplementedError()


def load_directed_signed_sample(thres=.61):
    raise NotImplementedError()


def load_directed_signed_sparse_sample(thres=.03):
    raise NotImplementedError()


def load_signed_sparse_sample(thres=.06):
    raise NotImplementedError()

# NBS samples


def load_sample_group_qball():
    q = np.load(op.join(MAT_DIR, 'sample_group_qball.npy'))
    return np.transpose(
        list(map(bc.utils.normalize, (q[:, :, i] for i in range(q.shape[2])))),
        (1, 2, 0))


def load_sample_group_dsi():
    d = np.load(op.join(MAT_DIR, 'sample_group_dsi.npy'))
    return np.transpose(
        list(map(bc.utils.normalize, (d[:, :, i] for i in range(d.shape[2])))),
        (1, 2, 0))


def load_sample_group_fmri():
    f = np.load(op.join(MAT_DIR, 'sample_group_fmri.npy'))
    import functools

    def compose(*functions):
        return functools.reduce(lambda f, g: lambda x: f(g(x)), functions)
    thresh_fun = functools.partial(bc.utils.threshold_proportional, p=.5)
    return np.transpose(list(map(compose(bc.utils.normalize, thresh_fun),
                                 (f[:, :, i] for i in range(f.shape[2])))),
                        (1, 2, 0))
