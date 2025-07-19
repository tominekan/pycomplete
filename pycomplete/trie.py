"""
This gives us the basic content for a suffix trie.

For runtime analysis purposes, we assume that the number of letters in the alphabet
is a, the number of words in the trie is n. 

TODO: THINK ABOUT RUNTIMES LOL

A lot of the walking down operations correspond to the height of the tree,
which should techincally be the length of the longest string for the uncompressed trie,
I think it should still be the same for the compressed trie.
"""

from trienode import TrieNode
from typing import Union

class Trie:
    def __init__(self, content: str) -> None:
        """
        FIXME: THIS IS WRONG LMFAOOO
        Assuming size of string is n. O(n) 
        Builds and compresses a Trie on all the set of words

        Parameters:
        ---
        content: str
            The content we are building the TrieNode structure on
        """

        words = content.split(" ")
        self._root = TrieNode("")

        for word in words:
            self.add_word(word)


    def add_word(self, word: str) -> None:
        """
        
        Adds a word to the Trie Structure.

        Parameters:
        ---
        word: str
            The word we want to add to the Trie structure
        """

        curr_node = self._root

        for char in word:
            if not curr_node.exists_child(char):
                curr_node.add_child(TrieNode(char))
                curr_node = curr_node.get_node_from_value(char)
        
        # NONE IS OUR END CHARACTER
        curr_node.add_child(TrieNode(None))
    

    def remove_word(self, word: str) -> None:
        """
        Removes `word` from the Trie structure. If the word doesn't exist in the Trie, then we raise ValueError.

        Parameters
        ---
        word: str
            The word specified
        """

        curr_node = self._walk_word(word)
        if curr_node == None:
            raise ValueError(f"\"{word}\" does not exist within Trie")
        
    

    def exists(self, word: str) -> bool:
        """
        Checks if `word` exists in the Trie structure. 

        Parameters:
        ---
        word: str
            The word we want to check the existence of
        """

        return self._walk_word(word) != None

    
    def _walk_word(self, word) -> Union[TrieNode, None]:
        """
        Walks down the suffix trie to find the node corresponding to the last letter of `word`

        Parameters
        ---
        word: str
            The word specified
        """

        curr_node = self._root

        for char in word:
            if curr_node.exists_child(char):
                curr_node = curr_node.get_node_from_value(char)
            else:
                return None
        
        # If there is no end word end node, then this implies
        # that there does not exist a word here
        if curr_node.exists_child(None):
            return curr_node
        else:
            return None
    

        

    
