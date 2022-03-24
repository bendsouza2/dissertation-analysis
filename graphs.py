import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline
import pandas as pd
import numpy as np

sample = pd.read_csv('eos_sample.csv')
one_y = list(sample['ac'])
one_x = list(sample['output'])

xnew = np.linspace(sample['output'].min(), sample['output'].max(), 50)
spl = make_interp_spline(one_x, one_y, k=7)
power_smooth = spl(xnew)

fig5 = plt.plot(xnew, power_smooth)
plt.title('Figure 5')
plt.xlabel('Output')
plt.ylabel('Average Cost')
frame1 = plt.gca()
frame1.axes.get_xaxis().set_ticks([])
frame1.axes.get_yaxis().set_ticks([])
plt.show()