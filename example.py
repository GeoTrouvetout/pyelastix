import numpy as np
import pyelastix
import matplotlib.pyplot as plt
from SliceViewer import multi_slice_viewer 



#def remove_keymap_conflicts(new_keys_set):
#    for prop in plt.rcParams:
#        if prop.startswith('keymap.'):
#            keys = plt.rcParams[prop]
#            remove_list = set(keys) & new_keys_set
#            for key in remove_list:
#                keys.remove(key)
#
#
#def multi_slice_viewer(volume):
#    remove_keymap_conflicts({'j', 'k'})
#    fig, ax = plt.subplots()
#    ax.volume = volume
#    ax.index = volume.shape[0] // 2
#    ax.imshow(volume[ax.index])
#    fig.canvas.mpl_connect('key_press_event', process_key)
#    plt.show()
#
#def process_key(event):
#    fig = event.canvas.figure
#    ax = fig.axes[0]
#    if event.key == 'j':
#        previous_slice(ax)
#        fig.canvas.draw()
#    elif event.key == 'k':
#        next_slice(ax)
#        fig.canvas.draw()
#    elif event.key == 'q':
#        plt.close()
#
#def previous_slice(ax):
#    volume = ax.volume
#    ax.index = (ax.index - 1) % volume.shape[0]  # wrap around using %
#    ax.images[0].set_array(volume[ax.index])
#    plt.title(str(ax.index))
#
#def next_slice(ax):
#    volume = ax.volume
#    ax.index = (ax.index + 1) % volume.shape[0]
#    ax.images[0].set_array(volume[ax.index])
#    plt.title(str(ax.index))





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


