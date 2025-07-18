"""
This gives us the basic content for a suffix trie.

For runtime analysis purposes, we assume that the number of letters in the alphabet
is a, the number of words in the trie is n. 

TODO: first we need to develop trie nodes lol
"""

class Trie:
    def __init__(self, content):
        """
        Assuming size of string is n. O(n)
        Builds and compresses a Trie on all the set of words
        """
        words = content.split(" ")
        words.split()

    def add_word(self, word):
        """
        Adds a word to the Suffix trie.
        """