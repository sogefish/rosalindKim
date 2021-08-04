#Problem: Computing GC Content

#The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.
#DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.
#In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

#Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
#Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

def printList(list):
    for elem in list:
        print(elem)

def highGC():
    file = open("rosalind_gc.txt", "r")
    tempGC = 0
    seq = ""
    seqList = []
    nameList = []
    gcList = []

    for line in file:
        if(line[0] == ">"):
            nameList.append(line.strip('\n'))
            seqList.append(seq)
            seq = ""
        else:
            seq += ''.join(line.splitlines())
    seqList.append(seq)
    seqList.pop(0)

    for seqs in seqList:
        g = seqs.count("G")
        c = seqs.count("C")
        tempGC = (g + c) / (len(seqs)) * 100
        gcList.append(tempGC)


    #printList(nameList)
    #printList(seqList)
    #printList(gcList)

    i = gcList.index(max(gcList))
    print(nameList[i] + " " + str(gcList[i]))


def highGCBetter():
    file = open('rosalind_gc.txt', 'r')

    max_gc_name, max_gc_content = '', 0

    buf = file.readline().rstrip()
    while buf:
        seq_name, seq = buf[1:], ''
        buf = file.readline().rstrip()
        while not buf.startswith('>') and buf:
            seq = seq + buf
            buf = file.readline().rstrip()
        seq_gc_content = (seq.count('C') + seq.count('G'))/float(len(seq))
        if seq_gc_content > max_gc_content:
            max_gc_name, max_gc_content = seq_name, seq_gc_content

    print('%s\n%.6f%%' % (max_gc_name, max_gc_content * 100))
    print(f"hello world {max_gc_name}! {max_gc_content}")
    file.close()

highGCBetter()