"""
Writen by joe.couto@abaeternum.com last revision 2FEB2022
Start the program from an Anaconda command prompt: python AbAAposStats.py
INPUT: a text file containing a multiple sequence alignment of antibody
variable regions.
OUTPUT: two .csv files with aminoacid frequency data at each framework and cdr position (roughly imgt);
The first csv file has the real numbers and the second has the percentages.  See below for an example of
an input file.
You can generate V-region Ab aligments on my site Abaeternum.com in the Tools tab.
The code can be easily modified to accomotade other proteins.
"""

oriA,seqA,R,K,H,D,E,S,T,N,Q,A,V,I,L,M,F,Y,W,G,C,P,B,X,Z,d = ([] for i in range(26))
inFile = input("input file name (input.txt): ") or "input.txt"
o1File = input("AA frequencies output file  name (aafrq.csv): ") or "aafrq.csv"
o2File = input("AA percent frequencies output file name (aapercfrq.csv): ") or "aapercfrq.csv"

try:
    with open(inFile) as f:     
        for line in f:
            oriA.append(line)
except FileNotFoundError:
    print('No such file')


for ele in oriA:
    xA = ele.split(":")
    seqA.append(xA[1].rstrip("\n"))

for j in range(len(seqA[0])):
    R.append([i[j] for i in seqA].count('R'))
    K.append([i[j] for i in seqA].count('K'))
    H.append([i[j] for i in seqA].count('H'))
    D.append([i[j] for i in seqA].count('D'))
    E.append([i[j] for i in seqA].count('E'))
    S.append([i[j] for i in seqA].count('S'))
    T.append([i[j] for i in seqA].count('T'))
    N.append([i[j] for i in seqA].count('N'))
    Q.append([i[j] for i in seqA].count('Q'))
    A.append([i[j] for i in seqA].count('A'))
    V.append([i[j] for i in seqA].count('V'))
    I.append([i[j] for i in seqA].count('I'))
    L.append([i[j] for i in seqA].count('L'))
    M.append([i[j] for i in seqA].count('M'))
    F.append([i[j] for i in seqA].count('F'))
    Y.append([i[j] for i in seqA].count('Y'))
    W.append([i[j] for i in seqA].count('W'))
    G.append([i[j] for i in seqA].count('G'))
    C.append([i[j] for i in seqA].count('C'))
    P.append([i[j] for i in seqA].count('P'))
    B.append([i[j] for i in seqA].count('B'))
    X.append([i[j] for i in seqA].count('X'))
    Z.append([i[j] for i in seqA].count('Z'))
    d.append([i[j] for i in seqA].count('-'))

posfreqD = {"R":R,"K":K,"H":H,"D":D,"E":E,"S":S,"T":T,"N":N,"Q":Q,"A":A,"V":V,"I":I,"L":L,"M":M,"F":F,"Y":Y,"W":W,"G":G,"C":C,"P":P,"B":B,"X":X,"Z":Z,"d":d}

out1="Aa,f0,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f11a,f11b,f11c,f11d,f12,f13,f14,f15,f16,f17,f18,f19,f20,f21,f22,f23,f24,f25,f26,c27,c28,c29,c30,c31,c32,c33,c34,c35,c36,c37,c38,f39,f40,f41,f42,f43,f44,f45,f46,f47,f48,f49,f50,f51,f52,f53,f54,f55,c56,c57,c58,c59,c60,c60a,c60b,c61,c62,c63,c64,c65,f66,f67,f68,f69,f70,f71,f72,f73,f74,f75,f76,f77,f78,f79,f80,f81,f82,f83,f84,f85,f86,f87,f88,f89,f90,f91,f92,f93,f94,f95,f96,f97,f98,f99,f100,f101,f102,f103,f104,c105,c106,c107,c108,c109,c110,c111,c111a,c111b,c111c,c111d,c111e,c111c,c111g,c111h,c111i,c111j,c111k,c111l,c112,c113,c114,c115,c116,c117,c118,f119,f120,f121,f122,f123,f124,f125,f126,f127,f128"+"\n"
for ele in posfreqD.keys():
    out1 += ele + "," + ','.join([str(x) for x in posfreqD[ele]]) + "\n"
f = open(o1File, "w")
f.write(out1)
f.close()

posprctD = posfreqD
L = R[1]+K[1]+H[1]+D[1]+E[1]+S[1]+T[1]+N[1]+Q[1]+A[1]+V[1]+I[1]+L[1]+M[1]+F[1]+Y[1]+W[1]+G[1]+C[1]+P[1]+B[1]+X[1]+Z[1]+d[1]

for ky in posprctD.keys():
    t = []
    for e in posprctD[ky]:
        t.append(round(100*e/L,1))
    posprctD[ky] = t
    
out2="Aa,f0,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f11a,f11b,f11c,f11d,f12,f13,f14,f15,f16,f17,f18,f19,f20,f21,f22,f23,f24,f25,f26,c27,c28,c29,c30,c31,c32,c33,c34,c35,c36,c37,c38,f39,f40,f41,f42,f43,f44,f45,f46,f47,f48,f49,f50,f51,f52,f53,f54,f55,c56,c57,c58,c59,c60,c60a,c60b,c61,c62,c63,c64,c65,f66,f67,f68,f69,f70,f71,f72,f73,f74,f75,f76,f77,f78,f79,f80,f81,f82,f83,f84,f85,f86,f87,f88,f89,f90,f91,f92,f93,f94,f95,f96,f97,f98,f99,f100,f101,f102,f103,f104,c105,c106,c107,c108,c109,c110,c111,c111a,c111b,c111c,c111d,c111e,c111c,c111g,c111h,c111i,c111j,c111k,c111l,c112,c113,c114,c115,c116,c117,c118,f119,f120,f121,f122,f123,f124,f125,f126,f127,f128"+"\n"
for ele in posprctD.keys():
    out2 += ele + "," + ','.join([str(x) for x in posprctD[ele]]) + "\n"
f = open(o2File, "w")
f.write(out2)
f.close()

"""
The input text file should look like this.
Make sure there are no colons : in the name part of the sequence an that all seqs are the same length with dashes and IUPAC amino-acids
>huVH_TEL1:-QVQLVQSGA-E----VKKPGQSLRISCKGAGYSF----STYWIGWVRQMPGKGLEWMGIIYPD----DSDTRYSPSFE-GQVTISVDKSITTAYLHWSSLKASDTAIYYCARLVG---------------GAPAYWGQGTLVTVSS
>huVH_M61':------------------------KISCKGSGYSF----TSYWIGWVRQMPGKGLEWMGIIYPG----DSDTRYSPSFQ-GQVTISADKSISTAYLQWSSLKASDTAMYYCARRRYMG----------YGDQAFDIWGQGTMVTVSS
>huVH_F19L:-QVQLQQSGP-G----LVKPSQTLSLTCAISGDSVS--SNSAAWNWIRQSPSRGLEWLGRTYYR---SKWYNDYAVSVK-SRITINPDTSKNQFSLQLNSVTPEDTAVYYCARELGDAF----------------------------
>huVH_L16':-QVQLQQSGP-G----LVKPSQTLSLTCAISGDSVS--SNSAAWNWIRQSPSRGLEWLGRTYYR---SKWYNDYAVSVK-SRITINPDTSKNQFSLQLNSVTPEDTAVYYCARELG---------------DAFDIWGQGTMVTVSS
"""

