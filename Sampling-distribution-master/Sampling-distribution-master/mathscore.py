import random
import csv
import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
df=pd.read_csv("Sampling-distribution-master/mathscore.csv")
data=df["Math_score"].tolist()
fig=ff.create_distplot([data],["Math Scores"],show_hist=False)
fig.show()
mean=statistics.mean(data)
std_devation=statistics.stdev(data)
print(mean)
print(std_devation)
