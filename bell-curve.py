import random
import plotly.express as pe
import plotly.figure_factory as pff
import statistics

addition = []
serial = []
for i in range (0,100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    add = dice1 + dice2
    addition.append(add)
    serial.append(i)

total=0

for i in addition:
    total=total+i

print(float(total/100))
digram2 = pff.create_distplot([addition],["Result"])
digram2.show()

print(addition)
print(serial)

digram = pe.bar(x=addition,y=serial)
digram.show()

mean=statistics.mean(addition)
median=statistics.median(addition)
mode=statistics.mode(addition)
sd=statistics.stdev(addition)
print(mean)
print(median)
print(mode)
print(sd)

cal = mean - sd
cal2 = mean + sd
print(cal)
print(cal2)