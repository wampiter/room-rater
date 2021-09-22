'''Create new data folders with organization applied'''
import os
from shutil import copyfile, move
from glob import glob

from room_rate.data.dataset import get_rating

dir_path = os.path.dirname(os.path.realpath(__file__))
data_path = os.path.join(dir_path, '../../../data')
savedir = os.path.join(dir_path, 'rated_images')
outdir = os.path.join(data_path, 'rated_images_no0')

def remove_zeros(indir=savedir, outdir=outdir, bad_ratings = (0,)):
    '''
    indir: input directory of images
    outdir: output directory with badly rated images removed
    bad_ratings: the ratings for which to remove images
    '''
    os.mkdir(outdir)
    imnames = glob(os.path.join(indir, '*.png'))
    for imname in imnames:
        rating = get_rating(imname)
        if rating not in bad_ratings:
            name = imname.split('/')[-1]
            copyfile(imname, os.path.join(outdir, name))

def train_test_split(folder=outdir, split=1/4):
    """
    Move all images in folder into sub-folders train and test
    Split is the fraction of images moved to test
    Test uses the most recent tweets, train tweets are older
    """
    for name in ['test', 'train']:
        os.mkdir(os.path.join(folder, name))
    fnames = sorted(glob(os.path.join(folder, '*.png')))
    l_test = int(len(fnames) * split)
    for fname in fnames[:l_test]:
        name = fname.split('/')[-1]
        move(fname, os.path.join(folder, 'test', name))
    for fname in fnames[l_test:]:
        name = fname.split('/')[-1]
        move(fname, os.path.join(folder, 'train', name))

if __name__ == '__main__':
    remove_zeros()
    train_test_split()
