def high(x):
    lookup = "abcdefghijklmnopqrstuvwxyz"
    words = x.split()
    
    weights = []
    
    for word in words:
        weight = 0
        for char in word:
            weight += (lookup.find(char)+1)
        weights.append(weight)
    
    ind = weights.index(max(weights))
    
    return words[ind]

#https://www.codewars.com/kata/57eb8fcdf670e99d9b000272
"""
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
"""