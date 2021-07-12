def searchKnuthMorris(pattern,text):
    """
    searchKnuthMorris function uses the Knuth Morris Pratt algoritm to perform pattern matching.
    Core function of this module.

    Args:
        pattern (str): pattern (to be searched)
        text (str): text 

    Raises:
        Exception: pattern not of type string
        Exception: text not of type string

    Returns:
        list(integers): contains the indexes where the pattern is found in the text
    """
    if isinstance(pattern, str) == False:
        raise Exception("The pattern is not of type string")
    if isinstance(text,str) == False:
        raise Exception("The text is not of type string")
    if pattern is None or text is None or pattern == "" or text == "":
        raise Exception("One of the strings is not defined correctly")

    i = 0
    j = 0

    # First, we compute the LPS array
    arrayLPS = computeLPSArray(pattern)

    result = list()
    
    # Check character by character the text 
    # NOTE: differently from the naive approach, that would
    # require us to go back and re-analyze parts of the text
    # that we previously analyzed, in this approach
    # the i index is never decremented, allowing us to 
    # examine the string text just once
    while i < len(text):      
        # If the two characters match, increment both indexes
        if text[i] == pattern[j]:
            i += 1
            j += 1
        
        # If we were able to match the whole pattern, 
        # store the index where the pattern starts. 
        if j == len(pattern):
            result.append(i-j)
            j = arrayLPS[j-1]
        
        # Otherwise if they do not match and j is not equal to 0, check
        # the value stored in the previous cell [j-1] and let j get
        # that value
        elif text[i] != pattern[j]:
            if j!=0:
                j = arrayLPS[j-1]
            # Otherwise (if they do not match and j is equal to 0) increment i
            else:
                i += 1
    return result

def computeLPSArray(pattern):
    """
    Utility function to calculate the LPS (Longest Proper Prefix that is also a Suffix) array.

    Args:
        pattern (str): pattern

    Raises:
        Exception: pattern not of type string

    Returns:
        array: the LPS array
    """
    if isinstance(pattern, str) == False:
        raise Exception("The pattern is not of type string")
    if pattern is None or pattern == "":
        raise Exception("Pattern is not defined correctly")
    
    i = 0
    j = 1
    
    # Create an empty array, filled with 0.
    # IMPORTANT: since the 1st value of the array must be 0,
    # the index j (used to fill the array) will start from 1.
    arrayLPS = [0]*len(pattern)
    
    # Fill out the array
    while j < len(pattern):
        # If the current characters match, increment i, assign
        # to array[j] the new value of i, then increment i
        if pattern[i] == pattern[j]:
            i += 1
            arrayLPS[j] = i
            j += 1
        # If the current characters do not match and i is equal to 0
        # it means that for the current character, the current prefix 
        # that is also a suffix has length 0, so we put 0 in our array
        elif i == 0:
            arrayLPS[j] = 0
            j += 1
        # If the current characters do not match but i is different 
        # from 0, we need to check the value that is in the i-1 position
        # and assign it to i, without incrementing j (because we want to
        # check whether the characters corresponding to our new i and old j
        # are a match)
        else:
            i = arrayLPS[i-1]
    return arrayLPS

text = "trentatre trentini entrarono a trento"
pattern = "tre"
#KMPSearch(pattern,text)
print(searchKnuthMorris(pattern,text))