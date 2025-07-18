# PyComplete

An autocomplete tool written in python. 

## Thoughts
I'd need
- [ ] A Trie structure to autocomplete the current word typed
    - [ ] Figure closest complete word (leaf) to current letter (node) (BFS) 
- [x] A first-order Markov chain to predict the next word based on the likeliest word
- [ ] An autocomplete


### Notes
All of our runtime analyses work with expected runtimes, not worst-case runtimes.