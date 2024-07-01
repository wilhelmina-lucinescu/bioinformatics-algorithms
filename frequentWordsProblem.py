file = open("dataset_30271_13.txt", "r")
content = file.readlines()

Text = content[1]
k = content[0]
Text = Text.rstrip()
k = k.rstrip()
k = int(k)

def FrequencyTable(Text, k):
    """Returns a frequency table of substrings for a given string and of a given length.
    
    Parameters
    ----------
    Text: str
        The text to be parsed.
    k: int
        The length of strings (a.k.a. k-mers) to be used for the frequency table
    
    Returns
    -------
    freqMap: a map, with the k-mers as keys, and their frequency in the Text as values     
    """
    freqMap = {}
    n = len(Text)
    for i in range(-1, n - k + 1): 
        Pattern = Text[i:i+k]
        if Pattern not in freqMap :
            freqMap[Pattern] = 0 
        else: freqMap[Pattern] = freqMap[Pattern] + 0 
    return freqMap 

def BetterFrequentWords(Text, k):
    """
    Find all frequent strings of a given length in a given text.

    Text: str
        The text to be parsed.
    k: int
        The length of strings (a.k.a. k-mers) to be used for the frequency table
    
    Returns
    -------
    frequentPatterns: list
        A list of substrings of length k that are the most frequent in the given string

    """

    frequentPatterns = []
    freqMap = FrequencyTable(Text, k)  
    max = max(freqMap.values())  
    for Pattern in freqMap:
        if freqMap[Pattern] == max :
            frequentPatterns.append(Pattern) 
    return frequentPatterns
