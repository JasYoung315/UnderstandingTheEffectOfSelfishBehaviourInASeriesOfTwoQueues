# This file was *autogenerated* from the file Analyse.sage.
from sage.all_cmdline import *   # import sage library
_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_5 = Integer(5); _sage_const_8 = Integer(8)
import os,sys,csv

def evalfail(string):
    try:
        return eval(string)
    except:
        return string

files = os.listdir('.')
files = [e for e in files if '.csv' in e]
print files
Data = []
for e in files :
    if '.csv' in e:
        infile = open(e,'rb')
        input = csv.reader(infile)
        Data.append( [[evalfail(i) for i in row] for row in input])
        infile.close()

for e in Data:
    r = plot([],axes_labels = ['$ \\lambda $','Average Cost'])

    r1data = []
    r2data = []
    r3data = []
    colors = rainbow(_sage_const_5 )

    for i in e:
        r1data.append([i[_sage_const_1 ],i[-_sage_const_1 ]])
        r2data.append([i[_sage_const_1 ],i[-_sage_const_2 ]])
        r3data.append([i[_sage_const_1 ],i[-_sage_const_3 ]])

    r += line(r3data,color = 'black', legend_label = 'Heuristic 1',linestyle = '-')
    r += line(r1data,color = 'black',   legend_label = 'Heuristic 2',linestyle = '--')
    r += line(r2data,color = 'black',  legend_label = 'Heuristic 3',linestyle = ':')

    r.save('./Exit%s.pdf' %e[_sage_const_0 ][_sage_const_8 ])
