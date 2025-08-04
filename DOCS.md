# Table of Contents

* [markovchain](#markovchain)
  * [MarkovChain](#markovchain.MarkovChain)
    * [\_\_init\_\_](#markovchain.MarkovChain.__init__)
    * [add\_item](#markovchain.MarkovChain.add_item)
    * [remove\_item](#markovchain.MarkovChain.remove_item)
    * [likeliest](#markovchain.MarkovChain.likeliest)
    * [contains](#markovchain.MarkovChain.contains)
* [trienode](#trienode)
  * [TrieNode](#trienode.TrieNode)
    * [\_\_init\_\_](#trienode.TrieNode.__init__)
    * [set\_parent](#trienode.TrieNode.set_parent)
    * [parent](#trienode.TrieNode.parent)
    * [add\_child\_node](#trienode.TrieNode.add_child_node)
    * [remove\_child\_node](#trienode.TrieNode.remove_child_node)
    * [remove\_child](#trienode.TrieNode.remove_child)
    * [exists\_child](#trienode.TrieNode.exists_child)
    * [get\_node](#trienode.TrieNode.get_node)
    * [get\_children\_values](#trienode.TrieNode.get_children_values)
    * [get\_children\_nodes](#trienode.TrieNode.get_children_nodes)
    * [is\_leaf](#trienode.TrieNode.is_leaf)
    * [num\_children](#trienode.TrieNode.num_children)
    * [value](#trienode.TrieNode.value)
* [pycomplete](#pycomplete)
  * [PyComplete](#pycomplete.PyComplete)
    * [\_\_init\_\_](#pycomplete.PyComplete.__init__)
    * [predict](#pycomplete.PyComplete.predict)
    * [add\_pair](#pycomplete.PyComplete.add_pair)
    * [add\_line](#pycomplete.PyComplete.add_line)
    * [save](#pycomplete.PyComplete.save)
    * [from\_text\_file](#pycomplete.PyComplete.from_text_file)
    * [load](#pycomplete.PyComplete.load)
* [chainset](#chainset)
  * [ChainSet](#chainset.ChainSet)
    * [\_\_init\_\_](#chainset.ChainSet.__init__)
    * [add](#chainset.ChainSet.add)
    * [create\_chain](#chainset.ChainSet.create_chain)
    * [remove](#chainset.ChainSet.remove)
    * [exists](#chainset.ChainSet.exists)
    * [likeliest](#chainset.ChainSet.likeliest)
* [trie](#trie)
  * [Trie](#trie.Trie)
    * [\_\_init\_\_](#trie.Trie.__init__)
    * [add\_word](#trie.Trie.add_word)
    * [remove\_word](#trie.Trie.remove_word)
    * [exists](#trie.Trie.exists)
    * [complete\_word](#trie.Trie.complete_word)

<a id="markovchain"></a>

# markovchain

This is the class for a first order Markov chains.

<a id="markovchain.MarkovChain"></a>

## MarkovChain Objects

```python
class MarkovChain()
```

<a id="markovchain.MarkovChain.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

Initializes a first order Markov chain with an empty set of items it points towards.

Parameters
---
name: Any
    This really be anything we use to identify the content.

<a id="markovchain.MarkovChain.add_item"></a>

#### add\_item

```python
def add_item(item: Any) -> None
```

O(1)

Adds an item to the Markov chain. 
If the item already exists, then it just increments the frequency counter associated with the item by 1.

Parameters
---
item: Any
    The item we want to add to the Markov chain

<a id="markovchain.MarkovChain.remove_item"></a>

#### remove\_item

```python
def remove_item(item: Any) -> None
```

O(log n) sorta kinda idk tbh

Decreases the frequency associated with item by 1.
If the item already has a zero frequency associated with it, then this program does nothing.
If the item doesn't exist, then we raise a KeyError

Finding runtime is a bit weird here because we're assuming that each call to remove_item is equally likely
to have any of the items as an input, so normally it'll take O(1) time, but when we call the likeliest item, it takes O(nlogn) time.
This means the total runtime over all the inputs is O(n) + O(nlogn), which is O(nlogn), divided by n is O(logn)

**Arguments**:

  ---
- `item` - Any
  The item we want to remove.

<a id="markovchain.MarkovChain.likeliest"></a>

#### likeliest

```python
def likeliest() -> Any
```

O(1)

Returns the item with the highest frequency.

<a id="markovchain.MarkovChain.contains"></a>

#### contains

```python
def contains(value: Any) -> bool
```

O(1)

Checks if the Markov chain contains `value`.

**Arguments**:

  ---
- `value` - Any
  The value we want to search for

<a id="trienode"></a>

# trienode

This allows us to create and manipulate Nodes within the Trie structure.

We're assuming that the value of the Node within a specific alphabet.
This implies that a certain TrieNode should NOT have a child.

For runtime analysis purposes, we're assuming that n = the number of children in the TrieNode.

<a id="trienode.TrieNode"></a>

## TrieNode Objects

```python
class TrieNode()
```

<a id="trienode.TrieNode.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: Any, parent: Union["TrieNode", None] = None) -> None
```

O(1)

Initializes a TrieNode instance with no children.

**Arguments**:

  ---
- `value` - Any
  The value of the new TrieNode
  
- `parent` - TrieNode | None
  The parent of the current TrieNode

<a id="trienode.TrieNode.set_parent"></a>

#### set\_parent

```python
def set_parent(new_parent: Union["TrieNode", None]) -> None
```

O(1)

Sets the parent `new_parent`

**Arguments**:

  ---
- `new_parent` - Any
  The new parent we want to set

<a id="trienode.TrieNode.parent"></a>

#### parent

```python
def parent() -> Union["TrieNode", None]
```

O(1)

Returns the parent

<a id="trienode.TrieNode.add_child_node"></a>

#### add\_child\_node

```python
def add_child_node(child: "TrieNode") -> None
```

O(1)

Adds a child node to this current node. It also automatically sets the parent of
this node to this node too. If the child TrieNode already exists, we raise ValueError.

Parameters
---
child: TrieNode
    The child TrieNode we want to add

<a id="trienode.TrieNode.remove_child_node"></a>

#### remove\_child\_node

```python
def remove_child_node(child: "TrieNode") -> "TrieNode"
```

O(1)

Removes `child` from set of children. It also sets the parent of `child` to None. 
Returns the child that we removed.
Raises ValueError if `child` is not a child of the TrieNode

Parameters
---
child: TrieNode
    The child TrieNode we want to remove

<a id="trienode.TrieNode.remove_child"></a>

#### remove\_child

```python
def remove_child(value: Any) -> "TrieNode"
```

O(1)

Removes `value` from the set of children. It also sets the parent of the child
associated to `value` to None. Returns the child TrieNode we removed.

Parameters
---
value: Any
    The value we want to remove

<a id="trienode.TrieNode.exists_child"></a>

#### exists\_child

```python
def exists_child(value: Any) -> bool
```

O(1)

Checks if a value exists within a child

Parameters
---
value: Any
    The value we want to check the existence of

<a id="trienode.TrieNode.get_node"></a>

#### get\_node

```python
def get_node(value: Any) -> "TrieNode"
```

O(1)

Returns the TrieNode corresponding to the value. If there is no child corresponding to value, 
we raise ValueError.

Parameters
---
value: Any
    The value we want to extract

<a id="trienode.TrieNode.get_children_values"></a>

#### get\_children\_values

```python
def get_children_values() -> list
```

O(n)

Returns all the values of the children Nodes

<a id="trienode.TrieNode.get_children_nodes"></a>

#### get\_children\_nodes

```python
def get_children_nodes() -> list
```

O(n)

Returns all the children Nodes

<a id="trienode.TrieNode.is_leaf"></a>

#### is\_leaf

```python
def is_leaf() -> bool
```

O(1)

Returns whether this current node is a leaf or not.

<a id="trienode.TrieNode.num_children"></a>

#### num\_children

```python
def num_children() -> int
```

O(1)

Returns the number of children the TrieNode has

<a id="trienode.TrieNode.value"></a>

#### value

```python
def value() -> Any
```

O(1)

Returns the current value of this TrieNode

<a id="pycomplete"></a>

# pycomplete

Now we're putting all the helper classes together in order to get the PyComplete module.

TODO: find out runtimes lol (should largely come from pycomplete/trie.py)

<a id="pycomplete.PyComplete"></a>

## PyComplete Objects

```python
class PyComplete()
```

<a id="pycomplete.PyComplete.__init__"></a>

#### \_\_init\_\_

```python
def __init__(text: str) -> None
```

Initializes an instance of PyComplete, which builds a Trie and develops the set of first-order Markov
chains on the text given


Parameters
---
text: str
    String containing the body of text we're trying to run PyComplete on

<a id="pycomplete.PyComplete.predict"></a>

#### predict

```python
def predict(text: str, num: int = 1) -> list
```

Predicts what the completed word (and following word) given a sequence of characters.
Returns a list containing the completed word, followed by the words after it.

if num < 1, we raise ValueError.

Parameters
---
text: str
    The given sequence of characters

num: int
    How many words ahead do we want to predict. By default, we predict one word ahead.

<a id="pycomplete.PyComplete.add_pair"></a>

#### add\_pair

```python
def add_pair(key: str, value: str) -> None
```

Adds a pair of words to the Markov chain.

Parameters
---
key: str
    The first word in the pair we want to add

value: str
    The second word in the pair

<a id="pycomplete.PyComplete.add_line"></a>

#### add\_line

```python
def add_line(line: str) -> None
```

Adds an entire line of text

Parameters
---
line: str
    The line we want to add to the autocomplete system

<a id="pycomplete.PyComplete.save"></a>

#### save

```python
def save(filepath: str) -> None
```

Saves the current PyComplete instance as a file. Raises ValueError if we're filepath is a directory.

Parameters
---
filepath: str
    The path to the file we want to handle

<a id="pycomplete.PyComplete.from_text_file"></a>

#### from\_text\_file

```python
@staticmethod
def from_text_file(filepath: str) -> "PyComplete"
```

Extracts the text from the file specified in the filepath and returns a PyComplete instance generated
from that text. We raise ValueError if the file we're reading is a directory or simply doesn't exist.

Parameters
---
filepath: str
    The path to the file we want to read

<a id="pycomplete.PyComplete.load"></a>

#### load

```python
@staticmethod
def load(filepath: str) -> "PyComplete"
```

Loads the PyComplete instance from the path. Raises ValueError if filepath is a directory.

Parameters
---
filepath: str
    The path to the file we want to read

<a id="chainset"></a>

# chainset

This allows us to use and manipulate a bunch first-order Markov chains.

<a id="chainset.ChainSet"></a>

## ChainSet Objects

```python
class ChainSet()
```

<a id="chainset.ChainSet.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

O(1)

Initializes an empty set first-order Markov chain.

<a id="chainset.ChainSet.add"></a>

#### add

```python
def add(key: Any, value: Any) -> None
```

O(1)

Adds `value` to the Markov chain keyed by `key`. The Markov chain does not exist, then we create a new one.

**Arguments**:

  ---
- `key` - Any
  The key of the Markov chain.
  
- `value` - Any
  The value we want to add

<a id="chainset.ChainSet.create_chain"></a>

#### create\_chain

```python
def create_chain(key: Any) -> None
```

O(1)

Creates a new Markov chain with a specific name. Raises ValueError if the key exists

**Arguments**:

  ---
- `key` - Any
  The key of the Markov chain.

<a id="chainset.ChainSet.remove"></a>

#### remove

```python
def remove(key: Any, value: Any) -> None
```

O(1)

Decrements an the frequency associated with value associated with the given key.

**Arguments**:

  ---
- `key` - Any
  The key of the Markov chain.
  
- `value` - Any
  The value we want to remove

<a id="chainset.ChainSet.exists"></a>

#### exists

```python
def exists(key: Any) -> bool
```

O(1)

Checks if the key exists in the set of chains

**Arguments**:

  ---
- `key` - Any
  The key to the Markov chain

<a id="chainset.ChainSet.likeliest"></a>

#### likeliest

```python
def likeliest(key: Any) -> Any
```

O(1)

Gets the likeliest value to occur given `key` occured. Raises ValueError if key doesn't exist.

**Arguments**:

  ---
- `key` - Any
  The key to the Markov chain

<a id="trie"></a>

# trie

This gives us the basic content for a suffix trie.

For runtime analysis purposes, we assume that the number of letters in the alphabet
is a, the number of words in the trie is n. 

TODO: THINK ABOUT RUNTIMES LOL

A lot of the walking down operations correspond to the height of the tree,
which should techincally be the length of the longest string for the uncompressed trie,
I think it should still be the same for the compressed trie.

<a id="trie.Trie"></a>

## Trie Objects

```python
class Trie()
```

<a id="trie.Trie.__init__"></a>

#### \_\_init\_\_

```python
def __init__(content: str) -> None
```

TODO: think about runtime
Assuming size of string is n. O(n) is super hard
Builds and compresses (NOT QUITE YET) a Trie on the

**Arguments**:

  ---
- `content` - str
  The content we are building the TrieNode structure on

<a id="trie.Trie.add_word"></a>

#### add\_word

```python
def add_word(word: str) -> None
```

Adds a word to the Trie Structure. If the word already exists, do nothing.

**Arguments**:

  ---
- `word` - str
  The word we want to add to the Trie structure

<a id="trie.Trie.remove_word"></a>

#### remove\_word

```python
def remove_word(word: str) -> None
```

Removes `word` from the Trie structure. If the word doesn't exist in the Trie, then we raise ValueError.

Parameters
---
word: str
    The word specified

<a id="trie.Trie.exists"></a>

#### exists

```python
def exists(word: str) -> bool
```

Checks if `word` exists in the Trie structure.

**Arguments**:

  ---
- `word` - str
  The word we want to check the existence of

<a id="trie.Trie.complete_word"></a>

#### complete\_word

```python
def complete_word(chars: str, num: int = 2) -> list
```

Finds the words closest to the sequence of characters specified in `chars`.

Parameters
---
chars: str
    The sequence of characters we want to search

num: int
    The number of words we want to get. Generally speaking, the more words want to get, the longer this method will run.
    By default, we want to suggest 2 words.

