def findCompDNA(dna) :
    compStrand = []
    for letter in dna:
        match letter:
            case 'A':
                compStrand += 'T'
            case 'T':
                compStrand += 'A'
            case 'C':
                compStrand += 'G'
            case 'G':
                compStrand += 'C'
            case _:
                print("No DNA strand provided")
    revcompStrand = ''.join(reversed(compStrand))
    return revcompStrand

## Alternative:
def ReverseComplement(dna_string):
    rev = dna_string[::-1]
    comp_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G':'C'}
    rev_comp = ''
    for base in rev:
        rev_comp += comp_dict[base]
    return rev_comp

def OverlappingPatternMatching(Pattern, Genome):
    positions = []
    pattern_length = len(Pattern)
    genome_length = len(Genome)
    for i in range(genome_length - pattern_length + 1):
        if Genome[i:i + pattern_length] == Pattern:
            positions.append(i)
    print(positions)
    return positions

def FindClumps(Text, k, L, t):
    Patterns = []
    n = len(Text)
    for i in range(0, n- L):
        slid_window = Text[i:i + L]
        freqMap = FrequencyTable(slid_window, k)
        for item in freqMap:
            if freqMap[item] >= t:
                Patterns.append(item)
    unique_Patterns = set(Patterns)
    print(unique_Patterns)
    return unique_Patterns