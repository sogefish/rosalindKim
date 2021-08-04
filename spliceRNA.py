#Problem: RNA Splicing

#After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.

#Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.
#Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)

import transcribeDNA as tDNA
import translateRNA as tRNA

def splice():
    dna = ''
    introns = []
    first = True
    file = open('rosalind_splc.txt','r')

    buf = file.readline().rstrip()
    while buf:
        buf = file.readline().rstrip()
        while not buf.startswith('>') and buf:
            if(first):
                dna += buf
            else:
                introns.append(buf)
            buf = file.readline().rstrip()
        first = False
    file.close()

    for intron in introns:
        dna = dna.replace(intron, '')
    print(dna)
    return(tRNA.translate(tDNA.transcribe(dna)))


print('\n' + splice())