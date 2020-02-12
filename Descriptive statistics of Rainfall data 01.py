# A traial to apply basic statitics
#

# Import packages
import numpy as np, pandas as pd, matplotlib.pyplot as plt, statistics, seaborn as sns

# Read data
DF = pd.read_excel('station kh _ Adel.xlsx',sheet_name='Data')

# Select Data
Suez = DF['Suez']
#print(Suez)

# Formating Histogram image
sns.set()
plt.hist(Suez,bins=11)
plt.xlabel('Annual maximum daily rainfall (mm)')
plt.xlim(0,50)
plt.ylim(0,70)
plt.ylabel('numper of years')
plt.title('Histogram of Annual maximum daily rainfall (mm)')
#plt.show()

# simple discriptive statistics

print("the mean rainfall over Suez is %2.2f mm " %statistics.fmean(Suez))   #https://www.python-course.eu/python3_formatted_output.php
print(pd.DataFrame.describe(Suez))



