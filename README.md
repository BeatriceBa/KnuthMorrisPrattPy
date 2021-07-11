# KnuthMorrisPrattPy

In string computation, the pattern matching problem is the problem of finding all the occurences of a pattern (string) P, in a text (string) S.

The Knuth Morris Pratt algorithm is used to solve pattern matching problems, by employing the observation that when a mismatch occurs, the word itself embodies sufficient information to determine where the next match could begin, thus bypassing re-examination of previously matched characters. 

## Description

The searchKnuthMorris function takes as input two strings:
* Pattern string
* Text string

And returns all the occurrences of the string Pattern in the string Text (specifically, it returns the index of the string Text where the string Pattern is found)

