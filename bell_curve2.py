import plotly.figure_factory as pff
import pandas as pd
import csv
import statistics

df = pd.read_csv(r"D:/python/py/bell_curve.csv")
digram = pff.create_distplot([df["Weight(Pounds)"].tolist()],["Weight"])
#digram.show()

Weightlist=df["Weight(Pounds)"].tolist()

wmean=statistics.mean(Weightlist)
wmedian=statistics.median(Weightlist)
wmode=statistics.mode(Weightlist)
sd=statistics.stdev(Weightlist)

print(wmean)
print(wmedian)
print(wmode)
print(sd)

cal = wmean - sd
cal2 = wmean + sd

print(cal)
print(cal2)

newlist=[]

for i in Weightlist:
    if(i>cal and i<cal2):
        newlist.append(i)

l1=len(newlist)
l2=len(Weightlist)

print("newlist is {}".format(len(newlist)))
print(l2)

oldlist=[q for q in Weightlist if q > cal and q < cal2]
print("oldlist is {}".format(len(oldlist)))
print("newlist is {} oldlist is {}".format(len(newlist),len(oldlist)))

per=(l1/l2)*100
print(per)

cal3=wmean - 2*sd
cal4=wmean + 2*sd

newlist2=[]

for a in Weightlist:
    if(a>cal3 and a<cal4):
        newlist2.append(a)

l3=len(newlist2)

oldlist2=[w for w in Weightlist if w>cal3 and w<cal4]
print("newlist2 is {} oldlist2 is {}".format(len(newlist2),len(oldlist2)))

per2=(l3/l2)*100
print(per2)

cal5 = wmean - 3*sd
cal6 = wmean + 3*sd

newlist3=[]

for b in Weightlist:
    if(b>cal5 and b<cal6):
        newlist3.append(b)



l4 = len(newlist3)

per3=(l4/l2)*100
print(per3)