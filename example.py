import numpy as np
import pyelastix
import matplotlib.pyplot as plt
from SliceViewer import multi_slice_viewer 




immov = np.load("MovImage_mod.npy")
imfix = np.load("FixImage_mod.npy")

print(immov.shape)

params = pyelastix.get_default_params("RIGID")
#params.MaximumNumberOfIterations = 200
#params.FinalGridSpacingInVoxels = 10
#params.Metric = "AdvancedMeanSquares"



immov_deformed, field = pyelastix.register(immov, imfix, params, verbose=3)

print()
print(field)
print()
print(immov_deformed.shape)
immov_deformed = immov_deformed/(immov_deformed.max()/255.0)

np.save("MovImage_mod_registered.npy", immov_deformed)

multi_slice_viewer( ( immov_deformed/np.max(immov_deformed) )  )


