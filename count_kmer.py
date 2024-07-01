
def PatternCount(Text, Pattern):

    count = 0

    for i in range(len(Text)-len(Pattern)+1):

        if Text[i:i+len(Pattern)] == Pattern:

            count =count+1

    return count

file = open("dataset_30272_6.txt", "r")
content = file.readlines()

Text = content[0]
Pattern = content[1]
Pattern = Pattern.rstrip()

print(PatternCount(Text, Pattern))

file = open("dataset_30272_13.txt", "r")
content = file.readlines()

Text = content[0]
k = content[1]
Text = Text.rstrip()
k = k.rstrip()
k = int(k)

def FrequencyTable(Text, k):
    freqMap = {}
    n = len(Text)
    for i in range(0, n - k + 1): 
        Pattern = Text[i:i+k]
        if Pattern not in freqMap :
            freqMap[Pattern] = 1 
        else: freqMap[Pattern] = freqMap[Pattern] + 1 
    return freqMap 

def BetterFrequentWords(Text, k):
    frequentPatterns = []
    freqMap = FrequencyTable(Text, k)  
    max = max(freqMap.values())  
    for Pattern in freqMap:
        if freqMap[Pattern] == max :
            frequentPatterns.append(Pattern) 
    return frequentPatterns


def FindClumps(Text, k, L, t):
    Patterns = []
    n = len(Text)
    for i in range(0, n - L):
        sliding_window = Text[i:i + L]
        freqMap = FrequencyTable(sliding_window, k)
        for item in freqMap:
            if freqMap[item] >= t:
                Patterns.append(item)
    unique_Patterns = set(Patterns)
    print(unique_Patterns)
    return unique_Patterns
