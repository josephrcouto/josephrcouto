"""
Writen by joe.couto@abaeternum.com last revision 9FEB2022
Start the program from an Anaconda command prompt: python AbBindingCurves.py
INPUT: a csv file containing binding data (see format at the bottom of this code).
OUTPUT1: adjustable pyplot with all data sets in a single plot.  To  plot
         datasets individually type any character on the last prompt
OUTPUT2: the user command prompt shows the best fit parameters
EXAMPLE: see Tools/Python on my website Abaeternum.com.
INPUT PARAMETERS: respond to the prompts or accept the default values
    Input file name: type in the file name including the file extension
                     comma-delimited (see format at the bottom of this code), 
                     or just RETURN to accept default file name: input.csv
    Best fit equation: type in 3, 4, 5, or 0 and RETURN or just RETURN to accept default (5)
        3par : y=R+(L-R)/(1+(x/k))            L,R-left & right plateaus  k-EC50
        4par : y=R+(L-R)/((1+(x/k)**S))       S-Hill Slope
        5par : y=R+(L-R)/((1+(x/k)**S)**A)    A-Asymmetry
        0Skip: data will be plotted without a best fit curve
        Note: if you can't get a fit for one or more of the datasets try another equation.  
    Legend position: type in one the following and RETURN or just RETURN to accept default (best)
        upper right     lower right     center right    right          
        upper left      lower left      center left     best
        upper center    lower center    center 
    All-in-one or Individual plots: the default is all-in-one      
"""
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
import numpy as np
import scipy.optimize as opt
import math
import warnings
warnings.filterwarnings('ignore')
parameters = ["L", "R", "k", "S", "A"]
inFile   = input("o - Input file name (default = input.csv): ") or "input.csv"
eqChoice = input("o - Best fit equation 3par 4par 5par 0none (default = 4par): " or "4")
legendpos = input("o - Legend position upper left, lower right, center right, ... etc (default = best): ") or "best"
individualPlot = input("o - Plot individual or (default = multiple) : ") or False

if "3" in eqChoice:
    eqChoice = "3par"
    print("3par y=R+(L-R)/(1+(x/k))")
    def func(x,L,R,k):      
        return R+(L-R)/(1+(x/k))
elif "5" in eqChoice:
    eqChoice ="5par"
    print("5par y=R+(L-R)/((1+(x/k)**S)**A)")
    def func(x,L,R,k,S,A):
        return R+(L-R)/((1+(x/k)**S)**A)
elif "0" in eqChoice:
    eqChoice="0none"
    print("no best fit analysis will be done")
else:
    eqChoice = "4par"
    print("4par y=R+(L-R)/((1+(x/k)**S))")
    def func(x,L,R,k,S):
        return R+(L-R)/((1+(x/k)**S))
oriA = []
dataA = []
try:
    with open(inFile) as f:     
        for line in f:
            oriA.append(line.rstrip("\n|\t"))
except FileNotFoundError:
    print('No such file')
for ele in oriA:
    iniA = ele.split(",")
    dataA.append(iniA)
col = 1
nbrColmns = len(dataA[0])
nbrRows   = len(dataA)
color = iter(cm.rainbow(np.linspace(0, 1, nbrColmns)))

while col<nbrColmns:
    xA = []
    yA = []
    for row in range(nbrRows):
        if (dataA[row][col] != ""):
            xA.append(dataA[row][0])
            yA.append(dataA[row][col])
    xA.pop(0)
    dataSet = yA.pop(0)
    xA2 = np.asfarray(xA,float)
    yA2 = np.asfarray(yA,float)
    nxtcolor = next(color)
    if eqChoice=="0none":
        plt.semilogx(xA2, yA2, marker=".", c=nxtcolor,label=dataSet)
        col += 1
        if individualPlot != False:
            plt.legend(loc=legendpos, frameon=False)
            plt.show()
    else:
        plt.semilogx(xA2, yA2, ".", c=nxtcolor,label=dataSet)
        col += 1
        try:
            optimizedParameters, pcov = opt.curve_fit(func, xA2, yA2, p0=None)
        except RuntimeError:
            print(dataSet + "CURVE-FIT NOT POSSIBLE WITH " +  eqChoice + " EQUATION")
            if individualPlot != False:
                plt.legend(loc=legendpos, frameon=False)
                plt.show()
            continue
        logStart = int(math.log(min(xA2),10)) - 1
        logEnd   = int(math.log(max(xA2),10)) + 1
        xA2 = np.logspace(logStart, logEnd, num=50, endpoint=True, base=10.0, dtype=None, axis=0)
        O = optimizedParameters
        plt.semilogx(xA2, func(xA2, *optimizedParameters), c=nxtcolor) 
        tempout = dataSet + " "
        for i in range(len(O)):
            tempout += parameters[i] + ":" + f"{O[i]:.2e}" + " "
        print(tempout)
        if individualPlot != False:
            plt.legend(loc=legendpos, frameon=False)
            plt.show()
if individualPlot == False: 
    plt.legend(loc=legendpos, frameon=False)
    plt.show()

"""
INPUT: Enter your data into an spreadsheet and save as .csv
Top  row: x, Ab1, Ab2, Ab3, ...etc
Below the top row enter x-values and readings for each Ab
Data mus be COMMA-DELIMITED (.csv file).
x=0 is not allowed because this will be a semi-log plot  
No particular data order is required.
option 1
x	    Ab1	     Ab2
0.001	0.00
0.01	0.01
0.26	0.21
0.51	0.36
4.10	0.87
524 	1.07		
0.001			0.00
0.01			0.00
1.02			0.37
4.10			0.70
32.7			1.03
524 			1.05
1048			1.00

option 2

x	    Ab1	     Ab2
0.001	0.00    0.00
0.01	0.01    0.00
1.02			0.37
0.26	0.21
0.51	0.36
4.10	0.87    0.70
32.7			1.03
524 	1.07    1.05		
1048			1.00	
"""