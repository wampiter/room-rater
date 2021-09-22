'''pytorch dataset (RatedImageDataset) for loading rated image data'''
from glob import glob
import os
from torch.utils.data import Dataset
from torchvision import io

def get_rating(imname):
    '''pull rating from image name string'''
    rating = imname.split("_")[-1]
    rating = int(rating.split(".")[0])
    return rating

class RatedImageDataset(Dataset):
    '''Rated Image Dataset'''

    def __init__(self, images_dir, transform=None):
        '''
        For loading rated image dataset (after downloaded)
        Args:
            images_dir (string): Directory with images
            transform (callable)
        '''
        self.images_dir = images_dir
        self.transform = transform
        path = os.path.join(images_dir, '*.png')
        self.inames = sorted(glob(path))

    def __len__(self):
        return len(self.inames)

    def __getitem__(self, idx):
        iname = self.inames[idx]
        image = io.read_image(iname)
        rating = get_rating(iname)
        if self.transform is not None:
            image = self.transform(image)
        return image, rating
