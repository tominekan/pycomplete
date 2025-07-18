"""
This allows us to use and manipulate a bunch first-order Markov Chains.
"""
from typing import Any

class FOMarkov:
    def __init__(self) -> None:
        """
        Initializes a first order Markov chain with an empty set of items it points towards.

        Parameters
        ---
        name: Any
            This really be anything we use to identify the content.
        """

        self.children = {}
        self.likeliest = None
        self.max_freq = 0
    
    def add_item(self, item: Any) -> None:
        """
        O(1)

        Adds an item to the Markov chain. 
        If the item already exists, then it just increments the frequency counter associated with the item by 1.

        Parameters
        ---
        item: Any
            The item we want to add to the Markov chain
        """

        if (item not in self.children):
            self.children[item] = 1
        else:
            self.children[item] += 1

        if (self.children[item] > self.max_freq):
            self.max_freq = self.children[item]
            self.likeliest = item
    

    def remove_item(self, item: Any) -> None:
        """
        O(1)

        Decreases the frequency associated with item by 1. 
        If the item already has a zero frequency associated with it, then this program does nothing.
        If the item doesn't exist, then we raise a KeyError

        Parameters:
        ---
        item: Any
        """
        if (item in self.children):
            self.children[item] = max(self.children[item] - 1, 0)
        
        raise KeyError(f"{item} does not exist in the Markov Chain.")
    
    def get_likeliest(self) -> Any:
        """
        O(1)

        Returns the item with the higest frequency. 
        """
        return self.likeliest


class MarkovChain:
    def __init__(self) -> None:
        """
        O(1)

        Initializes an empty set first-order Markov chain.
        """

        self.chains = {}
    
    def add_pair(self, key: Any, value: Any):
        """
        O(1)

        Adds `value` to the Markov chain keyed by `key`. The Markov chain does not exist, then we create a new one.
        """
    
    def create_chain(self, key: Any):
        """
        O(1)

        Creates a new Markov chain with a specific name. Raises ValueError if the key exists
        """
        if (key not in self.chains):
            self.chains[key] = FOMarkov()
        