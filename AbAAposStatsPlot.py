
"""
Writen by joe.couto@abaeternum.com last revision 3FEB2022
Start the program from an Anaconda command prompt: python AbAAposStatsPlot.py
INPUT: You must have a text file named "input.txt" - see below at the end of this
script for an example of input data or to test the script.
OUTPUT:
   the x axis has the positions named on the first line of input.txt
   the y axis is the residue percent frequency at each position
   each Aa residue is plotted as a colored marker
       e.g. if position f5 has Lys and Asp at 60% and 20%  incidences, respectively,
            a blue K and a red D marker will be plotted over x=f5 at y=60 and y=20
       you can see an example of the output in my website abaeternum.com in the TOOLS tab: Python section 
"""
import matplotlib.pyplot as plt
import numpy as np
iA = []
cD = {"R":'b',"K":'b',"H":'b',"D":'r',"E":'r',"S":'m',"T":'m',"N":'m',"Q":'m',"A":'k',"V":'k',"I":'k',"L":'k',"M":'k',"F":'k',"Y":'c',"W":'c',"G":'c',"C":'#eda621',"P":'c',"B":'m',"X":'k',"Z":'m',"d":'#f2f1d0'}
with open("input.txt") as f:     
    for line in f:
        iA.append(line.rstrip("\s|\n|\t"))
x = iA.pop(0).split("\t")
x.pop(0)
for line in iA:
    xA = line.split("\t")
    m = xA.pop(0)
    y = np.asfarray(xA,float)
    plt.plot(x, y, marker=r"$ {} $".format(m),color=cD[m],linestyle="" )
plt.xlabel("Ab framework (f) and CDR (c) positions")
plt.ylabel("% Aa frequency")
plt.show() 

"""
The input.txt file must be in the same directory as AbAAposStatsPlot.py and contain
input data taken from one of the .csv files outputed by AbAAposStats.py and formatted as follows:
(Make sure the first column has the IUPAC residue codes, except for d, which stands for dash (-)
in the original a seq alignement proccessed by AbAAposStats.py)
Aa	f39	f40	f41	f42	f43	f44	f45	f46	f47	f48	f49	f50	f51	f52	f53	f54	f55
R	0	0.2	0	0	99.1	0.2	0	0	0	0.2	0.2	0	0	0	0	0.2	0
K	0	0	0	0	0	0	0	0	0	36.5	0	0	0.2	0	0	0	0
H	0	0	0	0	0.4	0.4	0	0	0	0	0	0	0	0	0	0	0.2
D	0	0	0	0	0	0	0	0	0	0	0	0	0.4	0	0	0	0.4
E	0	0.2	0	0	0	0	0	0	0.9	1.8	3.1	0	98.9	0	0	0.2	0
S	0.2	55.6	0	0	0	0	0	0	0	0.9	0	0	0	0.4	0	0	0.7
T	0	4	0	0	0	0	0.9	0	0	0	0	0	0	0	0	0	14.3
N	0	3.1	0	0	0	0	0	0	0	59.9	0	0	0	0	0.2	0	0
Q	0	0.2	0	0	0	98.4	0	0	0	0.2	0	0	0.2	0	0	0	0
A	0	0.9	0	0	0	0	98.9	0	0	0	0	0	0	0	0	2.5	30.5
V	24.7	0	0	99.1	0	0	0	0	0.2	0	0	0	0	0	0.9	0.2	3.4
I	43.5	13.7	0	0.2	0	0	0	0	0	0	0	0	0	0	98	0	11.2
L	0.7	0	0.2	0	0	0.4	0	0.2	0	0	0	99.8	0	0.2	0.2	0	0.2
M	30.5	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0.7
F	0.2	0	0	0	0	0	0	0	0	0	0	0	0	0	0.4	0	7.8
Y	0	0.2	0	0	0	0	0	0	0	0	0	0	0	20.2	0	0	7.8
W	0	0	99.6	0	0	0	0	0	0	0	0	0	0	78.9	0	0	1.1
G	0	2.5	0	0.4	0	0	0	0	98.7	0	96.4	0	0	0	0	96.6	1.3
C	0	19.1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	20
P	0	0	0	0	0.2	0.2	0	99.6	0	0	0	0	0	0	0	0	0
B	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
X	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
Z	0	0	0	0	0	0	0	0	0	0.2	0	0	0	0	0	0	0
d	0.2	0.2	0.2	0.2	0.2	0.2	0.2	0.2	0.2	0.2	0.2	0.2	0.2	0.2	0.2	0.2	0.2
"""

