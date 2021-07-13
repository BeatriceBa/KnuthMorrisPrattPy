# KnuthMorrisPrattPy


## Description

In string computation, the pattern matching problem is the problem of finding all the occurences of a pattern (string) P, in a text (string) S.

The Knuth Morris Pratt algorithm is used to solve pattern matching problems, by employing the observation that when a mismatch occurs, the word itself embodies sufficient information to determine where the next match could begin, thus bypassing re-examination of previously matched characters. 

## Functions

### Perform the KMP search
The searchKnuthMorris function takes as input two strings, the pattern string and text string. It returns all the occurrences of the string Pattern in the string Text (specifically, it returns the index of the string Text where the string Pattern is found)

`print(searchKnuthMorris("ll","apellefigliodapollofeceunapalladipelledipollo"))`

### Create LPS
computeLPSArray is a utility function to calculate the LPS (Longest Proper Prefix that is also a Suffix) array. It is used to perform the KMP search

`print(computeLPSarray("CIAOCIAOCIAO"))`

## How to..?

Move into the directory where there is the Wheel file *knuthMorrisPratt-0.0.1-py3-none-any.whl*

Create a virtual environment (commands listed are for Windows)
`py -m venv env`
`.\env\Scripts\activate`

Install the Wheel file via pip
`pip install knuthMorrisPratt-0.0.1-py3-none-any.whl`

Test the package
`py`
`from knuthMorrisPratt import searchKnuthMorris`
`print(searchKnuthMorris("ll","apellefigliodapollofeceunapalladipelledipollo"))`

When you finish, deactivate the virtual environment
`deactivate`

## Requires

* Python3
* pip


