#!/usr/bin/env python

# Given four letters, come up with an acceptable random word

class Dictionary(object):
  def __init__(self, words_file_path):
    with open(words_file_path) as file:
      for line in file:
        print line

def main():
  dictionary = Dictionary('/usr/share/dict/words')

if __name__ == '__main__':
  main()
