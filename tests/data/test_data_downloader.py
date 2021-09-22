'''Tests for data_downloader.py'''
import os
from glob import glob
from matplotlib import pyplot as plt
import shutil

from room_rate.data import data_downloader

dir_path = os.path.dirname(os.path.realpath(__file__))

#Test strings/ratings for data extractor
extractor_tests = {
    '8/10': 8,
    'aasfd2/10': 2,
    '////0/10': 0,
    '    10/10': 10,
    '???.': None,
    '23/10': None,
    'a/10': None,
}

def test_extract_rating():
    '''tests for extract_rating()'''
    for content, rating in extractor_tests.items():
        assert data_downloader.extract_rating(content) == rating

def test_download_tweets():
    '''test download_tweets() (and also save_im())'''
    savedir = os.path.join(dir_path, 'download_test')
    try:
        data_downloader.download_tweets(max_tweets = 1,
                                        savedir = savedir,
                                        save_size = (128, 128))
        im_path = glob(os.path.join(savedir, '*.png'))[0]
        im = plt.imread(im_path)[..., :3]
        assert im.shape == (128, 128, 3)
    except:
        print('Shape: ' + str(im.shape))
        raise
    finally:
        shutil.rmtree(savedir) #cleanup
