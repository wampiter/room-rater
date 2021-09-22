from pathlib import Path
import os, shutil

from room_rate.data import data_organizer

dir_path = os.path.dirname(os.path.realpath(__file__))
sample_dirname = os.path.join(dir_path, 'sample_organize')
sample_names = [f'{i}_{i}.png' for i in range(2)]

def make_sample_dir():
    '''Make example data dir for other testing'''
    os.mkdir(sample_dirname)
    for sample_name in sample_names:
        fpath = os.path.join(sample_dirname, sample_name)
        Path(fpath).touch()

def cleanup(dname=sample_dirname):
    '''Delete the sample dir'''
    shutil.rmtree(dname)

def test_remove_zeros():
    try:
        odir = os.path.join(dir_path, 'odir')
        make_sample_dir()
        data_organizer.remove_zeros(sample_dirname, odir)
        files = sorted(os.listdir(odir))
        assert files == sample_names[1:]
    except:
        print(files)
        raise
    finally:
        cleanup(odir)
        cleanup()

def test_train_test_split():
    try:
        make_sample_dir()
        data_organizer.train_test_split(sample_dirname, split = .5)
        train = os.path.join(sample_dirname, 'train')
        test = os.path.join(sample_dirname, 'test')
        split_spot = int(len(sample_names)/2)
        train = sorted(os.listdir(train))
        test = sorted(os.listdir(test))
        assert train == sample_names[split_spot:]
        assert test == sample_names[:split_spot]
    except:
        print('train: ' + str(train))
        print('test: ' + str(test))
        raise
    finally:
        cleanup()
