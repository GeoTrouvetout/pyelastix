import numpy as np
import matplotlib.pyplot as plt

def remove_keymap_conflicts(new_keys_set):
    for prop in plt.rcParams:
        if prop.startswith('keymap.'):
            keys = plt.rcParams[prop]
            remove_list = set(keys) & new_keys_set
            for key in remove_list:
                keys.remove(key)


def multi_slice_viewer(volume):
    remove_keymap_conflicts({'j', 'k'})
    fig, ax = plt.subplots()
    ax.volume = volume
    ax.index = volume.shape[0] // 2
    ax.imshow(volume[ax.index])
    fig.canvas.mpl_connect('key_press_event', process_key)
    plt.title(str(ax.index))
    plt.show()

def process_key(event):
    fig = event.canvas.figure
    ax = fig.axes[0]
    if event.key == 'j':
        previous_slice(ax)
        fig.canvas.draw()
    elif event.key == 'k':
        next_slice(ax)
        fig.canvas.draw()
    elif event.key == 'q':
        plt.close()

def previous_slice(ax):
    volume = ax.volume
    ax.index = (ax.index - 1) % volume.shape[0]  # wrap around using %
    ax.images[0].set_array(volume[ax.index])
    plt.title(str(ax.index))

def next_slice(ax):
    volume = ax.volume
    ax.index = (ax.index + 1) % volume.shape[0]
    ax.images[0].set_array(volume[ax.index])
    plt.title(str(ax.index))




def main():
    immov = np.load("MovImage_Mk1o1_transf_mod.npy")
    imfix = np.load("FixImage_Mk1o1_mod.npy")
    immov_reg = np.load("MovImage_mod_registered.npy")
    print(np.max(immov))
    print(np.max(imfix))
    print(np.max(immov_reg))

    multi_slice_viewer(imfix-immov_reg)

if __name__ == '__main__':
    main()




