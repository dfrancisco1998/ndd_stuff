from graspy.simulations.simulations import sample_edges, p_from_latent
from graspy.simulations.rdpg_corr import rdpg_corr
import numpy as np


from platform import python_version
print("The python Version is: ", end = "")
print(python_version())

np.random.seed(1234)
X = np.random.dirichlet([1, 1], size=5)
Y = None


x = rdpg_corr(X, Y, 0.3, rescale=False, directed=False, loops=False)
print("This is the output after calling rdpg_corr from rdpg_corr.py")
print(x)
