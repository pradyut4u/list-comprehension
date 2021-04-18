import plotly.express as pe
import plotly.figure_factory as pff
import pandas as pd
import csv

df = pd.read_csv(r"D:/python/py/bell_curve.csv")
digram2 = pff.create_distplot([df["Height(Inches)"].tolist()],["Height"],show_hist=False)
digram2.show()