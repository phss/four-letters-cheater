#!/usr/bin/env python

# Given four letters, come up with an acceptable random word
import random
from collections import defaultdict

class Dictionary(object):
  def __init__(self, words_file_path):
    self.dict = defaultdict(list)

    with open(words_file_path) as file:
      for line in file:
        word = line.strip()
        self.dict[self._str_key(word)].append(word)

  def find_any_matching(self, letters):
    key = self._str_key(letters)
    options = self.dict[key]
    if not options:
      return None
    else:
      return random.choice(options)

  def _str_key(self, s):
    return ''.join(sorted(s.lower()))


def find_word(letters):
  dictionary = Dictionary('/usr/share/dict/words')
  print dictionary.find_any_matching(letters)

if __name__ == '__main__':
  find_word("load")
