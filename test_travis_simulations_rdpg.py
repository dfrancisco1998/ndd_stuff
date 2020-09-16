from graspy.simulations.simulations import sample_edges, p_from_latent
from graspy.simulations.rdpg_corr import rdpg_corr
from graspy.simulations.simulations import rdpg
import numpy as np



np.random.seed(1)
X = np.random.dirichlet([1, 1], size=5)
x = rdpg(X, loops=False)

print(x)
