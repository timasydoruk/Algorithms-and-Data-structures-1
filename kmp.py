
def kmp_search(pattern: str, text: str) -> list[int]:
    """Searches for a given pattern in the given input text using the KMP algorithm.

    Args:
        pattern (str): The pattern to search for.
        text (str): The text to search in.

    Raises:
        TypeError: If `pattern` or `text` are not strings.
        ValueError: If `pattern` or `text` are empty.

    Returns:
        list[int]: A list of indices of the first character of each match of `pattern` in `text`.
    """
    #! Usage of str.find and/or str.index results in 0 points
    #Veryfying the input
    if not isinstance(pattern, str) or not isinstance(text, str):
        raise TypeError("Pattern and text must be strings")
    if not pattern or not text:
        raise ValueError("Pattern and text cannot be empty")
    #Defining the matches to store the found indices
    matches = []
    text_length = len(text)
    pattern_length = len(pattern)
    #Defyining the failure table 
    failure_table = kmp_failure_table(pattern)
    #Variables to itarate through both the text and the pattern 
    text_index = 0
    pattern_index = 0
    #Searching loop until the end is found
    while text_index < text_length:
        #If the characters match, move both indices forward
        if text[text_index] == pattern[pattern_index]:
            text_index += 1
            pattern_index += 1
        #If the characters match the pattern if found
        if pattern_index == pattern_length:
            #Calculate the index and append the matches
            matches.append(text_index - pattern_index)
            #Move the pattern index back according to the failure table
            pattern_index = failure_table[pattern_index - 1]
        #If the characters do not match and the end of the text is not reached
        elif text_index < text_length and text[text_index] != pattern[pattern_index]:
            #If we had the sub-match before move back the pattern index according to the failure table
            if pattern_index != 0:
                pattern_index = failure_table[pattern_index - 1]
            #If we are stuck at the beginning, move forward
            else:
                text_index += 1
    return matches

    
    


def kmp_failure_table(pattern: str) -> list[int]:
    """Calculates and returns the table of the kmp failure function.

    Quote from the Lecture slides:
    ---
    [We use] a failure function f, that indicates how much of the last comparison can be reused if it fails.

    f(j) is defined as the length of the longest prefix of the pattern P[0,...,j], which is also the suffix of P[1,...,j].
    ---

    Pre-calculate f(j) for each index in `pattern` and return it as a list.

    Returns:
        list[int]: A list of failure function values.
    """
    #Defining the failure table and the lentgth of the pattern
    l = len(pattern)
    #Vizualize the table of zeros with the given length 
    failure_table = [0] * l
    #Defining the longest prefix-suffix length
    longest_prefix_suffix = 0
    #Iterating through the pattern from index 1 to the end 
    for j in range(1, l):
        #If the characters do not match and there is the sub-match 
        #We update the longest prefix-suffix according to the previous value
        while longest_prefix_suffix > 0 and pattern[longest_prefix_suffix] != pattern[j]:
            longest_prefix_suffix = failure_table[longest_prefix_suffix - 1]
        #If the characters match, proceed with the current prefix 
        if pattern[longest_prefix_suffix] == pattern[j]:
            longest_prefix_suffix += 1
        #Update the failure table with the longest prefix-suffix length
        failure_table[j] = longest_prefix_suffix
    return failure_table

    
    