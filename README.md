# PyComplete

An autocomplete tool written in Python. This is largely a proof of concept.
I might rewrite in C++ if I get this working, might not tho, who knows.


## TODOS
- [ ] Add caching/save-file for PyComplete instances
- [ ] Build API for PyComplete (likely using FastAPI)
    - [ ] Need to think about architecture for PyComplete API first
- [ ] Figure out asymptotic runtimes for `trie.py` and `pycomplete.py` 
- [ ] Find a service to cache PyComplete instances

### Notes
- To be frank, I'm not sure what direction this project should be taking
- All of our runtime analyses are expected runtimes, not worst-case runtimes 
    - **NOTE**: Sometimes my analyses are all fucked up and I try to explain what I did lol
- I think I want to be more consistent with the exceptions I raise.

**API Architecture**:
- **MVP:** User sends request and text to process a body of text
- User sends request, if ID is not specified, then we develop a new trienode