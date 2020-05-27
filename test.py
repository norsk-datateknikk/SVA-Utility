import numpy as np
from csv2network import *
import matplotlib.pyplot as plt

n = csv2network('LISN_S21.csv')
plt.figure()
n.plot_s_db()
plt.grid()

plt.show()