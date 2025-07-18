"""
This gives us the basic content for a suffix trie.

For runtime analysis purposes, we assume that the number of letters in the alphabet
is a, the number of words in the trie is n. 

TODO: THINK ABOUT RUNTIMES LOL
"""
from trienode import TrieNode

class Trie:
    def __init__(self, content):
        """
        Assuming size of string is n. O(n)
        Builds and compresses a Trie on all the set of words
        """

        words = content.split(" ")
        self._root = TrieNode("")

        

    def add_word(self, word):
        """
        
        Adds a word to the Trie Structure.
        """

        curr_node = self._root

        for char in word:
            if (not curr_node.exists_child(char)):
                curr_node.add_child(TrieNode(char))
                curr_node = curr_node.get_node_from_value(char)
        
        curr_node.add_child(TrieNode("end"))