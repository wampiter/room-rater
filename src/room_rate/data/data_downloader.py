"""Download tweets with ratings"""
import requests
from snscrape.modules.twitter import TwitterUserScraper, Photo
from tqdm import tqdm
import os
from PIL import Image
import io

dir_path = os.path.dirname(os.path.realpath(__file__))
savedir = os.path.join(dir_path, '../../../data/rated_images')

def extract_rating(content):
    '''
    Extract 0-10 rating from room rating tweet
    Return None if 0-10 rating not found
    '''
    try: #Try to extract 0-10 rating
        content = content.split('/10')[0] #rating is before the /10
        try:
            content = int(content[-2:])
        except ValueError: #first character could throwing us off
            content = int(content[-1:])
        assert content <= 10
        assert content >= 0
    except: #multiple exceptions
        content = None
    return content

def save_im(i, rating, image, savedir, size):
    '''
    Resize image number i to sizexsize and save with rating infilename
    and save in savedir
    '''
    image = Image.open(io.BytesIO(image.content))
    image = image.resize(size)
    image.save(savedir + '/%05d_%02d.png' % (i, rating))

def download_tweets(max_tweets = int(1e4),
                    savedir = savedir,
                    account = 'ratemyskyperoom',
                    save_size = (128, 128)):
    '''
    Download a maximum of max_tweets to savedir
    from twitter account at resolution save_size.
    savedir should not exist and will be created
    At some point may except 'ScraperException'. This is fine as long
    as enough (>3000) tweets have been downloaded.
    '''
    os.mkdir(savedir)
    tweets = TwitterUserScraper(account, False).get_items()
    j = 0 #count successful ratings downloads
    for tweet in tqdm(tweets):
        if not tweet.media: #don't bother if no image
            continue
        rating = extract_rating(tweet.content)
        if rating is None:
            continue #don't bothing if no rating
        for medium in tweet.media:
            if isinstance(medium, Photo):
                im = requests.get(medium.fullUrl)
                save_im(j, rating, im, savedir, save_size)
                j += 1
                break #should only be one image
        if j > max_tweets:
            break

if __name__ == '__main__':
    download_tweets()
