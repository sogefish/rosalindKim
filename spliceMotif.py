#Problem: Finding a Spliced Motif

#A subsequence of a string is a collection of symbols contained in order (though not necessarily contiguously) in the string (e.g., ACG is a subsequence of TATGCTAAGATC). The indices of a subsequence are the positions in the string at which the symbols of the subsequence appear; thus, the indices of ACG in TATGCTAAGATC can be represented by (2, 5, 9).
#As a substring can have multiple locations, a subsequence can have multiple collections of indices, and the same index can be reused in more than one appearance of the subsequence; for example, ACG is a subsequence of AACCGGTT in 8 different ways.

#Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.
#Return: One collection of indices of s in which the symbols of t appear as a subsequence of s. If multiple solutions exist, you may return any one.

def motif(s, t):
    ind = []
    track = 0
    for i, nuc in enumerate(s):
        if(track >= len(t)):
            break
        elif(nuc == t[track]):
            ind.append(i + 1)
            track += 1
    return tuple(ind)

def motif2(s, t):
    i = -1
    for c in t:
        i = s.find(c, i+1)
        print(i+1,)

seq = "GAGTGAATACTAGACTTACTCGGGTATGGGCAACACAAATGTTGGTCTACGACGACTTGTTAGACTTCAATACTGAGGCAAGCCCAGCCTGGTGACTCTTGATGACATGCATAATGTCCTGGTGACGGGCGTTGCGATACCGCCAGTAAGACGCTACTATAAGGGATCCAGATTAGAGTTCCTAGGCACGACACTTCGACCGACCAAATATCGCTGTGGTCTTCACTGCGCAAGTCCTTCCTGAATAAGGGCTGGTTTAGAATTGGTGGAAGCAATTATCAAAACTACGACTACGGGATGCCACTCCCTGAATATAATTTGGACGGATCTAACAATGATACAGCCATCAATGACAGATAACCTTAAATACAAGACCTGACTTCACGGAGGGCTATATACCATTCGTATCGATAGGTAGGAGTATACGAGCCCTTTATTACGTTAATGGGTATAGAGATAGATGCGTACCGAGCGGTACTCAGGTTGAGGGTAGCTTGTGGCCTATCGACTCCTCAGCCGGAATAGTCCGACCGAATTAATGGTTTTTACATCGCTCGGGCGGTCCAGTCAGTTGAGGCCCTTTTATTCCGGCAGGGGCTCGGTCACCAAACAGTGCGATCCACGACAATACAAAGTCACACGGACTGCCAGAGGTATATCTGCAGGTCTGTTTCTGAGTTAGGCTACGATGCCCAACCTAAGTTACCCTGGACGCTGTGGCCGAGACCTGCCTTGTGGGGAATGCTCCGCTCTACCAACGGCCTGAGCCACCACCAGCCAATCCAATAATCATTAACAACTTTACTACAAGGAGAGAAAGCCAGCATCGTCCGTCATCCCCGCAGCATAACCATTGAAGAGCGAAATGCCCGAGCATGGCGACTCGACCGTCAAATTTCTCAATGGAAGGGGGAGCGCTATGGCCGCAGTACAATGAAGCACTAATACGTGGAGAATTGGGCCAACTATACCCGCTTACTGTGAACTG"
sub = "GTCGAATGTTATCAGCGGAG"
print(motif(seq, sub))
