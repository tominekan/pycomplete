# PyComplete

An autocomplete tool written in Python. This is largely a proof of concept.
I might rewrite in C++ if I get this working, might not tho, who knows.

## TODOS
- [x] A Trie structure to autocomplete the current word typed
    - [x] Figure closest complete word (leaf) to current letter (node) (BFS-style) 
- [x] A first-order Markov chain to predict the next word based on the likeliest word
- [x] An autocomplete system that completes words using Trie data structures, and Markov chains to predict the next word.
    - Once the word has been completed, we can use a Markov chain predict the word right after that. Not quite sure how many words ahead we should go, I think one word ahead should be ok.
- [ ] Pretty fucking comprehensive testing for the methods I've implemented so far lol.
    - I know I'm likely getting something wrong and I don't want to get any hard to fix bugs.
- [ ] Implement a method to cache both Trie and ChainSet structures so we don't have to build it every time we want to use it
    - This will likely mean that I need to use the struct or pickle package, not sure yet though
- [ ] Maybe figure out a way to get this done over the cloud
    - [ ] Look at databricks


### Notes
- All of our runtime analyses are expected runtimes, not worst-case runtimes 
    - **NOTE**: Sometimes my analyses are all fucked up and I try to explain what I did lol
- I think I want to be more consistent with the exceptions I raise.
