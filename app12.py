import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Read the CSV file
my_data = pd.read_csv("health.csv")

# Group by Quality of Sleep and calculate count and percentage
my_data_summary = my_data.groupby('Quality of Sleep').size().reset_index(name='count')

my_data_summary['percentage'] = round((my_data_summary['count'] / my_data_summary['count'].sum()) * 100, 1)


# Define colors for the plot
darker_blues = ["lightblue", "#6baed6",  "#4292c6",  "#2171b5", "#08519c", "#08306b"]

# Calculate number of unique categories for the column "Quality of Sleep"
num_categories = len(my_data_summary['Quality of Sleep'].unique())
darker_blues = darker_blues[:num_categories]

# Create the pie chart
plt.figure(figsize=(10, 6))
patches, texts, autotexts = plt.pie(my_data_summary['count'], colors=darker_blues, autopct='%1.1f%%', wedgeprops={'linewidth': 1.5, 'edgecolor':'white'})
plt.title('Relationship Between Sleep Quality and Heart Rate Among Surveyed Individuals')


# print(my_data_summary['Quality Of Sleep'])
# Add legend
labels = ['{}'.format(i) for i in my_data_summary['Quality of Sleep']]
plt.legend(patches, labels, title="Quality of Sleep", loc="upper right", bbox_to_anchor=(1, 0, 0.2, 1))

plt.show()