#!/usr/bin/env python

# From an Android screen grab, extract the four letter images
from skimage import data, io, filters

def extract(file_path):
  image = io.imread(file_path)
  width, height = 120, 150
  image_dims = [(480, 980), (245, 1210), (715, 1210), (480, 1443)]

  for i, (x, y) in enumerate(image_dims):
    sub = image[y:(y+height), x:(x+width)]
    io.imsave("experiments/data/extracted_%d.png" % i, sub)

if __name__ == '__main__':
  extract('experiments/data/screen.png')
