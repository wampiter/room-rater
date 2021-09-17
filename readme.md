## About
This project attempts to rate images based on the aesthetic preferences learned from the training set. Specifically, the dataset I've used so far is (a few thousand of) [@ratemyskyperoom's](https://twitter.com/ratemyskyperoom) ratings of video-call rooms.

Initial testing shows some (weak) ability to predict ratings in the test set (the most recent ~750 rated room tweets):
![Test Results](imgs/Mean_Std_Results_MSELoss.png)

## Install
```
pip install -e .
```

## Use
Data downloading currently in src/room_rate/data/data_downloader.ipynb  #TODO change to module
Data manipulation in data/data_manipulation.ipybn #TODO change to module
Training and testing in notebooks/train.ipynb

Tests in test/ can be run with pytest

### Aditional TODO
- Experiments
    - Treat as classification (e.g. cross-entropy loss) instead of regression
    - Other architectures
    - Over/random-sampling to get (more) even representation across ratings
- Set up convenient inference flow
