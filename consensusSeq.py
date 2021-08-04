#Problem: Consensus and Profile

#A matrix is a rectangular table of values divided into rows and columns. An m×n matrix has m rows and n columns. Given a matrix A, we write Ai,j to indicate the value found at the intersection of row i and column j.

#Say that we have a collection of DNA strings, all having the same length n. Their profile matrix is a 4×n matrix P in which P1,j represents the number of times that 'A' occurs in the jth position of one of the strings, P2,j represents the number of times that C occurs in the jth position, and so on (see below).
#A consensus string c is a string of length n formed from our collection by taking the most common symbol at each position; the jth symbol of c therefore corresponds to the symbol having the maximum value in the j-th column of the profile matrix. Of course, there may be more than one most common symbol, leading to multiple possible consensus strings.

#Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
#Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

def printList(list):
    newList = map(str, list)
    return " ".join(newList).strip('\n')

def consensus():
    file = open('rosalind_cons.txt', 'r')
    buf = file.readline().rstrip()
    seqs = []

    join = 0
    track = -1
    while buf:
        buf = file.readline().rstrip()
        track += 1
        while not buf.startswith('>') and buf:
            if(join == 0):
                seqs.append(buf)
                join = 1
            else:
                seqs[track] += buf
                join = 0
            buf = file.readline().rstrip()
    long = len(max(seqs, key = len))  
    a = [0] * long
    c = [0] * long
    g = [0] * long
    t = [0] * long
    
    for x in range(len(seqs)):
        for y in range(long):
            if(y > len(seqs[x])-1):
                break
            if( seqs[x][y] == 'A'):
                a[y] += 1
            elif( seqs[x][y] == 'C' ):
                c[y] += 1
            elif( seqs[x][y] == 'G' ):
                g[y] += 1
            elif( seqs[x][y] == 'T' ):
                t[y] += 1

    cons = [-1] * long
    consSeq = [""] * long
    
    for i in range(long):
        if(a[i] > cons[i]):
            cons[i] = a[i]
            consSeq[i] = "A"
        if(c[i] > cons[i]):
            cons[i] = c[i]
            consSeq[i] = "C"
        if(g[i] > cons[i]):
            cons[i] = g[i]
            consSeq[i] = "G"
        if(t[i] > cons[i]):
            cons[i] = t[i]
            consSeq[i] = "T"
    consSeq = ''.join(consSeq)
    print(consSeq)
    print(f"A: {printList(a)}\nC: {printList(c)}\nG: {printList(g)}\nT: {printList(t)}")
    write = open('consensusSeq.txt', 'w')
    write.write(consSeq + "\nA: " + printList(a) + "\nC: " + printList(c) + "\nG: " + printList(g) + "\nT: " + printList(t))
    file.close()
    write.close()
consensus()