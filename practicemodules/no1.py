import seaborn as sb
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("annual-enterprise-survey-2020.csv")

val = data["value"]

lst = []
for x in range(len(val)):
    try:
        lst.append(int(val[x]))
    except:
        continue

arr = np.array(lst)
label = ["0-5000", "5000-10000", "10000-20000", "over 20000"]
color = ["purple", "pink", "violet", "red"]
explode = (0, 0.4, 0.4, 0.4)
newarr = np.array([
    (np.count_nonzero((arr >= 0) & (arr <= 5000))),
    (np.count_nonzero((arr > 5000) & (arr <= 10000))),
    (np.count_nonzero((arr > 10000) & (arr <= 20000))),
    (np.count_nonzero(arr > 20000))
])

plt.pie(newarr, labels=label, colors=color, explode=explode, shadow='true', autopct='%1.0f%%')

plt.show()
