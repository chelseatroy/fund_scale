import pandas as pd
import numpy as np
from fbprophet import Prophet
import matplotlib.pyplot as plt

df = pd.read_csv('SP500.csv')
df['y'] = np.log(df['y'])

m = Prophet(growth='linear')
m.fit(df)

future = m.make_future_dataframe(periods=30, freq='D')
fcst = m.predict(future)

m.plot(fcst);
m.plot_components(fcst);
plt.savefig('sp500.png')