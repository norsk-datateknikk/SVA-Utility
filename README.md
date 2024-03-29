# csv2network
Converts CSV files from Spectrum & Vector Network Analyzer to a Scikit RF network.

Note that the analyzer only saves the content visible on the screen. Ensure that the S21 dB mag and phase are visible.

By Norsk Datateknikk AS. Contact for consulting and product develpment at https://norskdatateknikk.no/

## Available on PYPI
[![Downloads](https://pepy.tech/badge/svautil)](https://pepy.tech/project/svautil)

https://pypi.org/project/svautil/
```
pip install svautil
```

## Example Code:

```python
import numpy as np
import svautil.vna as vna
import matplotlib.pyplot as plt

n = vna.csv2network('S21.csv', 'S21')
plt.figure()
n.plot_s_db()
plt.grid()

plt.show()
```

![Resulting Image](result.png)
