# csv2network
Converts CSV files from Sigilent Vector Spectrum Analyzers to a Scikit RF network.

By Norsk Datateknikk. Contact for consulting and product develpment at https://norskdatateknikk.no/

## Available on PYPI
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
