"""
brainconn: Brain Connectivity Toolbox in Python
"""
from .centrality import centrality as centrality_
from .clustering import clustering as clustering_
from .core import core as core_
from .degree import degree as degree_
from .distance import distance as distance_
from .generative import generative as generative_
from .modularity import modularity as modularity_
from .motifs import motifs as motifs_
from .physical_connectivity import physical_connectivity as phys_
from .reference import reference as reference_
from .similarity import similarity as similarity_
from .utils import teachers_round
from .nbs import nbs_bct
from .version import __version__

del (centrality_, clustering_, core_, degree_, distance_, generative_,
     modularity_, motifs_, phys_, reference_, similarity_, teachers_round,
     nbs_bct)

__all__ = ['__version__', 'centrality', 'clustering', 'core', 'degree',
           'distance', 'generative', 'modularity', 'motifs',
           'physical_connectivity', 'reference', 'similarity', 'utils',
           'nbs']
