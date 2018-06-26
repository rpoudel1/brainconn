"""
brainconn: Brain Connectivity Toolbox in Python
"""
from .centrality import centrality
from .clustering import clustering
from .core import core
from .degree import degree
from .distance import distance
from .generative import generative
from .modularity import modularity
from .motifs import motifs
from .physical_connectivity import physical_connectivity
from .reference import reference
from .similarity import similarity
from .utils import *  # teachers_round
from .nbs import *  # nbs_bct
from .version import __version__

del (centrality, clustering, core, degree, distance, generative, modularity,
     motifs, physical_connectivity, reference, similarity)
