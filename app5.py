import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Assuming my_data is a DataFrame containing your data
# Read the CSV file
my_data = pd.read_csv("health.csv")

# Define custom colors for genders
gender_colors = {"Male": "#6699FF", "Female": "#FF9966"}

# Create the plot
sns.catplot(data=my_data, x="BMI Category", hue="Gender", kind="count", height=6, aspect=1.5, palette=gender_colors)

# Add text annotations
ax = plt.gca()
for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', fontsize=9, color='black', xytext=(0, 5),
                textcoords='offset points')

# Set title and axis labels
plt.title("Distribution of BMI by Gender")
plt.xlabel("BMI")
plt.ylabel("Count")
plt.legend(title="Gender")

# Show the plot
plt.show()
