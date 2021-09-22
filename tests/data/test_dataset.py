from os import path

from room_rate.data.dataset import RatedImageDataset

def test_single_load():
    my_path = path.dirname(path.realpath(__file__))
    data_path = path.join(my_path, "sample_data")
    loader = RatedImageDataset(data_path)
    image, rating = loader[0]
    assert len(image.shape) == 3
    assert isinstance(rating, int)
