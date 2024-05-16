import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy.stats import gaussian_kde
from joypy import joyplot

# Read the CSV file
my_data = pd.read_csv("health.csv")


print(my_data['Age'].isna().sum())

# Define the breakpoints for Age groups
breaks = np.arange(my_data['Age'].min(), my_data['Age'].max()+1, 4)
print(breaks)

# Create Age groups
my_data['Age_Group'] = pd.cut(my_data['Age'], bins=breaks, labels=["{} - {}".format(i, i + 4) for i in breaks[:-1]], right=False)
# Create the Joyplot
# Create a new figure and axes with a specific size
fig, ax = plt.subplots(figsize=(10, 6))  # Change the numbers to adjust the width and height of the plot

# Create the Joyplot
joyplot(data=my_data, by='Age_Group', column='Stress Level', ax=ax, colormap=plt.cm.plasma, alpha=0.35, overlap=2)

plt.title("Distribution of Stress Levels by Age Group", y=0.9)
plt.xlabel("Stress Level")
plt.ylabel("Age Group")
plt.show()