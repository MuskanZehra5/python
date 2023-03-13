import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

weight = ['121lbs', '457lbs', '423lbs', '451lbs', '402lbs']
arr = []
for i in range(len(weight)):
    arr.append(int(weight[i][:-3]))

print(arr)
