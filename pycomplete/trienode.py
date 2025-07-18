"""
This allows us to create and manipulate Nodes within the Trie structure.

We're assuming that the value of the Node within a specific alphabet.
This implies that a certain TrieNode should NOT have a child
"""

from typing import Union, Any

class TrieNode:
    def __init__(self, value: Any, parent: Union["TrieNode", None] = None):
        """
        O(1)

        Initializes a TrieNode instance with no children.

        Parameters:
        ---
        value: Any
            The value of the new TrieNode
        
        parent: "TrieNode" | None
            The parent of the current TrieNode
        """

        self._value = value
        self._parent = parent

        self._children = {}
    
    def set_parent(self, new_parent: Union["TrieNode", None]):
        """
        O(1)

        Sets the parent `new_parent`

        Parameters:
        ---
        new_parent: Any
            The new parent we want to set
        """

        self._parent = new_parent
    
    def parent(self):
        """
        O(1)

        Returns the parent
        """

        return self._parent
    
    def add_child(self, child: "TrieNode"):
        """
        Adds a child node
        """
        self._children[child._value] = child
    