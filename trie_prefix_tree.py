#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#
class TrieNode:
    def __init__(self):
        self.end_mark = False
        self.next = [None] * 10 # up to 'j'

def add(root, s):
    current = root
    for i in range(len(s)):
        nw = ord(s[i]) - ord('a')
        # 's' is a prefix of a word already inserted into Trie
        if i == (len(s) - 1) and current.next[nw] is not None: 
            return False
        if current.next[nw] is None:
            current.next[nw] = TrieNode()
        # 's' is a prefix of a word already inserted into Trie
        current = current.next[nw]
        if current.end_mark:
            return False
    current.end_mark = True
    return True

def noPrefix(words):
    trie = TrieNode()
    for word in words:
        if not add(trie, word):
            print("BAD SET")
            print(word)
            return
    print("GOOD SET")
    
    

if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)

