from glob import glob
import os
from torch.utils.data import Dataset, DataLoader
from torchvision import io

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
        rating = iname.split("_")[-1]
        rating = int(rating.split(".")[0])
        if self.transform is not None:
            image = self.transform(image)
        return image, rating
