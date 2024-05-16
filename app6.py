import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Assuming my_data is a DataFrame containing your data
# Read the CSV file
my_data = pd.read_csv("health.csv")

# Convert BMI.Category to categorical with specified levels
my_data["BMI Category"] = pd.Categorical(my_data["BMI Category"], categories=["Normal", "Normal Weight", "Overweight", "Obese"], ordered=True)

# Define custom colors for BMI categories
bmi_colors = {"Normal": "#FF9999", "Normal Weight": "#FF9966", "Overweight": "#FF6600", "Obese": "#CC99FF"}

# Create the boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(data=my_data, x="BMI Category", y="Heart Rate", palette=bmi_colors)

# Set title and axis labels
plt.title("Heart Rate by BMI Category")
plt.xlabel("BMI Category")
plt.ylabel("Heart Rate")

# Remove legend
plt.legend().remove()

# Show the plot
plt.show()
