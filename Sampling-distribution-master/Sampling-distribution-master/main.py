import csv
import random
import statistics
from numpy import FLOATING_POINT_SUPPORT
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
df=pd.read_csv("Sampling-distribution-master/data.csv")
data=df["temp"].tolist()
population_mean=statistics.mean(data)
mean=statistics.mean(data)
#fig=ff.create_distplot([data],["temp"],show_hist=False)
#fig.show()
def show_fig(mean_list):
    df=mean_list
    fig=ff.create_distplot([data],["temp"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="mean"))
    fig.show()

