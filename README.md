# PyComplete

An autocomplete tool written in Python. Might rewrite in C++ if I get this working, might not tho, who knows.

## Thoughts
I'd need
- [ ] A Trie structure to autocomplete the current word typed
    - [ ] Figure closest complete word (leaf) to current letter (node) (BFS) 
- [x] A first-order Markov chain to predict the next word based on the likeliest word
- [ ] An autocomplete system that completes words using Trie data structures, and Markov chains to predict the next word.
    - [ ] The word autocomplete system should work by finding the closest leaf to the set of words so far.
        - [ ] This should work using a modified BFS algorithm
    - [ ] Once the word has been completed, we can use a Markov chain predict the word right after that. Not quite sure how many words ahead we should go, I think one word ahead should be ok.


### Notes
All of our runtime analyses work with expected runtimes, not worst-case runtimes.