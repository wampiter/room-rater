## About
This project attempts to rate images based on the aesthetic preferences learned from the training set. Specifically, the dataset I've used so far is (a few thousand of) [@ratemyskyperoom's](https://twitter.com/ratemyskyperoom) ratings of video-call rooms.

Initial testing shows some (weak) ability to predict ratings in the test set (the most recent ~750 rated room tweets):
![Test Results](imgs/Mean_Std_Results_MSELoss.png)

## Install
```
pip install -e .
```

If you wish to download data from twitter you will also need to install the developer version of snscrape:
```
pip3 install git+https://github.com/JustAnotherArchivist/snscrape.git
```
## Test
To test that the code is working run `pytest` from this directory:
```
pytest
```
Note that this currently assumes developer version of snscrape is installed.

## Use
You can download images from twitter by creating a data directory here `mkdir data`, then running
`python3 src/room_rate/data/data_downloader.py` (or import this module for more detailed options)

Remove ratings you want to exclude (e.g. 0) and sort into train/test sets by running `python3 src/room_rate/data/data_organizer.py`. (again, more details in module)

Training and testing in **notebooks/train.ipynb**

### Aditional TODO
- Experiments
    - Treat as classification (e.g. cross-entropy loss) instead of regression
    - Other architectures
    - Over/random-sampling to get (more) even representation across ratings
    - Use (scaled) sigmoid at output for regression (MSE) version
    - Fine-tune a trained model?
- Set up convenient inference flow
