# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 13:24:22 2022

@author: ACER
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

gas= pd.read_csv("C:\\Users\\ACER\\.spyder-py3\\gas_prices.csv")
gas
#relax

plt.title('Gas Prices over Time(in USD)')
#plt.figure(figsize=(8,5))
for country in gas:
    print(country)
    if country != 'Year':
        plt.plot(gas.Year,gas[country],marker=".",label=country)
#plt.plot(gas.Year,gas.USA,label='United states',marker=".")
#plt.plot(gas.Year,gas.Canada,label='Canada',marker=".")
#plt.plot(gas.Year,gas['South Korea'],label='S. Korea',marker=".") #some need to use this braket
plt.xticks(gas.Year) #displying ALL year in x axis
plt.xlabel("Year")
plt.ylabel("USD")
plt.legend() #need a label first
plt.show()