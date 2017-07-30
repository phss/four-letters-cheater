#!/usr/bin/env python

# From an Android screen grab, extract the four letter images
from skimage import io, color
from collections import Counter

def explode_color(image):
  flattened_image = image.reshape(-1)
  for i, p in enumerate(flattened_image):
    new_p = 1
    if p > 0.9:
      new_p = 0
    flattened_image[i] = new_p

def extract(file_path):
  image = io.imread(file_path)
  width, height = 120, 150
  image_dims = [(480, 980), (245, 1210), (715, 1210), (480, 1443)]

  for i, (x, y) in enumerate(image_dims):
    sub = image[y:(y+height), x:(x+width)]
    sub = color.rgb2gray(sub)
    explode_color(sub)
    io.imsave("experiments/data/extracted_%d.png" % i, sub)

if __name__ == '__main__':
  extract('experiments/data/screen.png')
