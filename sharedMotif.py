#Problem: Finding a Shared Motif

#A common substring of a collection of strings is a substring of every member of the collection. We say that a common substring is a longest common substring if there does not exist a longer common substring. For example, "CG" is a common substring of "ACGTACGT" and "AACCGTATA", but it is not as long as possible; in this case, "CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".
#Note that the longest common substring is not necessarily unique; for a simple example, "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".

#Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.
#Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

def motif():
    file = open('rosalind_lcsm.txt','r')
    buf = file.readline().rstrip()
    seq = [ '' for i in range(150) ]
    tracker = 0
    lcs = ""

    while buf:
        buf = file.readline().rstrip()
        while not buf.startswith('>') and buf:
            seq[tracker] += buf
            buf = file.readline().rstrip()
        tracker += 1
    seq = [x for x in seq if x]
    file.close()
    return long_substr(seq)

def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and is_substr(data[0][i:i+j], data):
                    substr = data[0][i:i+j]
    return substr

def is_substr(find, data):
    if len(data) < 1 and len(find) < 1:
        return False
    for i in range(len(data)):
        if find not in data[i]:
            return False
    return True

print(motif())