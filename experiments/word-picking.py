#!/usr/bin/env python

# Given four letters, come up with an acceptable random word
from collections import defaultdict

class Dictionary(object):
  def __init__(self, words_file_path):
    self.dict = defaultdict(list)

    with open(words_file_path) as file:
      for line in file:
        word = line.strip()
        self.dict[self._str_key(word)].append(word)
        
  def _str_key(self, s):
    return ''.join(sorted(s))


def main():
  dictionary = Dictionary('/usr/share/dict/words')

if __name__ == '__main__':
  main()
