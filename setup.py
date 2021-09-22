""" This file is used to create the package. """
from setuptools import setup, find_packages

setup(
    name='room_rate',
    package_dir={"": "src"},
    packages=find_packages('src'),
    author="Scott R. Johnston",
    install_requires=[
        'torch',
        'numpy',
        'torchvision',
        'pytest',
        'matplotlib',
        'tqdm',
        'Pillow',
    ],
)
