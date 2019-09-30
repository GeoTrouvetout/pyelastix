import numpy as np
import pyelastix

immov = np.load("MovImage_mod.npy")
imfix = np.load("FixImage_mod.npy")

print(immov.shape)

params = pyelastix.get_default_params()
params.MaximumNumberOfIterations = 200
params.FinalGridSpacingInVoxels = 10



immov_deformed, field = pyelastix.register(immov, imfix, params, verbose=3)

print(field)
