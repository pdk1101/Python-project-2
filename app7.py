import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file
my_data = pd.read_csv("health.csv")

pivot_table = my_data.pivot_table(index='Occupation', columns='BMI Category', aggfunc='size', fill_value=0)

cmap = sns.light_palette("blue", as_cmap=True)

plt.figure(figsize=(12, 8))
# Create the heatmap
sns.heatmap(pivot_table, cmap=sns.color_palette("ch:s=-.2,r=.6", as_cmap=True), fmt='d', annot=True)
plt.title('Relationship between Occupation and BMI Category')
plt.xlabel('BMI Category')
plt.ylabel('Occupation')

sns.set_theme()

plt.show()
