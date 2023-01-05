import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Data
df = pd.read_csv('data.csv')
# print(df.head(10))

x= df['area']
y= df['status']

# Linear regression
slope, intercept = np.polyfit(x, y, 1)
prediction_function = np.poly1d((slope, intercept))

# Plot data and prediction function
plt.plot(x, y, 'bo', x, prediction_function(x), 'k')
plt.show()
