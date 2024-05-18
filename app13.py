import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
def plot13():
    # Assuming my_data is a pandas DataFrame with columns 'Quality of Sleep' and 'Gender'
    # Read the CSV file
    my_data = pd.read_csv("health.csv")

    # Rename the column
    my_data.rename(columns={'Age_Group': 'Quality of Sleep'}, inplace=True)

    # Define custom color palette
    custom_palette = {"Male": "skyblue", "Female": "salmon"}

    # Create the plot
    g = sns.FacetGrid(my_data, col="Gender", height=6)
    g.map_dataframe(sns.histplot, x="Quality of Sleep", hue="Gender", discrete=True, palette=custom_palette)

    # Add annotations for count
    def annotate_counts(data, **kwargs):
        ax = plt.gca()
        for p in ax.patches:
            ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                        ha='center', va='center', fontsize=10, color='black', xytext=(0, 5),
                        textcoords='offset points')
    g.map_dataframe(annotate_counts)

    g.set_axis_labels("Quality of Sleep", "Count")
    g.set_titles("Distribution of Quality of Sleep by {col_name}")

    return plt.gcf()

