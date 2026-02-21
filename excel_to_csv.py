'''import pandas as pd
td = pd.read_csv("trans_data.csv")
td.describe()'''
import pandas as pd
import numpy as np
import matplotlib
import plotly
#%matplotlib inline

ts = pd.Series(np.random.randn(50), index = pd.date_range("today",periods = 50))
ts = ts.cumsum()
ts.plot()
