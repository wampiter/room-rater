'''Various helpful, shared things'''
from glob import glob
import os

def im_norm(im):
    """
    Convert image from 0 to 255 (int) to -1 to 1 (float)
    """
    return (im.float()/128 - 1).float()

def get_imnames(dirname):
    '''get all image names in directory'''
    names = []
    for ext in ['.jpg', '.png', '.JPG']:
        wild = '*' + ext
        new_names = sorted(glob(os.path.join(dirname, wild)))
        names = names + new_names
    return names
