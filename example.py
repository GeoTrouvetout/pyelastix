import numpy as np
import pyelastix
import matplotlib.pyplot as plt
from SliceViewer import multi_slice_viewer 
from pprint import pprint



#immov = np.load("MovImage_mod.npy")
#imfix = np.load("FixImage_mod.npy")
immov = np.load("MovImage_Mk1o1_transf_mod.npy")
imfix = np.load("FixImage_Mk1o1_mod.npy")
imfix = imfix/(imfix.max()/255.0)
immov = immov/(immov.max()/255.0)
#immov = np.max(immov) - immov
#imfix = np.max(imfix) - imfix

print(immov.shape)

params = pyelastix.get_default_params("RIGID")

params.MaximumNumberOfIterations = 1000
params.NumberOfResolutions = 10
params.Metric = "AdvancedMeanSquares"
params.AutomaticScalesEstimation = True
params.MaximumStepLength = 20.0 
params.DefaultPixelValue = 0


pprint(params.as_dict())




immov_deformed, field, transfo = pyelastix.register(immov, imfix, params, verbose=3)
#
#print()
print(transfo)
#print()
#print(immov_deformed.shape)
immov_deformed = immov_deformed/(immov_deformed.max()/255.0)
#
np.save("MovImage_mod_registered.npy", immov_deformed)
#
multi_slice_viewer( immov_deformed - immov )



