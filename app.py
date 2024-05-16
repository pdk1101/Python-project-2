import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def plot1():
    # Read the CSV file
    my_data = pd.read_csv("health.csv")

    # Get unique occupations and assign unique colors to each
    unique_occupations = my_data['Occupation'].unique()

    # Create a dictionary that maps each occupation to a unique color
    occupation_colors = sns.color_palette("husl", n_colors=len(unique_occupations))

    # Create a dictionary that maps each occupation to a unique color
    occupation_color_dict = dict(zip(unique_occupations, occupation_colors))

    gender_order = ["Male", "Female"]
    g = sns.FacetGrid(my_data, col="Occupation", col_wrap=4, height=4)

    # Map a bar plot onto the grid
    for occupation, color in occupation_color_dict.items():
        sns.barplot(data=my_data[my_data['Occupation'] == occupation], x="Gender", y="Sleep Duration", order=gender_order, estimator='mean', ci=None, color=color, ax=g.axes[unique_occupations.tolist().index(occupation)])

    # Set titles for each plot
    for ax, title in zip(g.axes.flat, unique_occupations):
        ax.set_title(title)

    # Set common title and axis labels
    g.fig.suptitle("Relationship between Gender, Occupation, and Sleep Duration", y=1.05)

    # Adjust the layout
    plt.tight_layout()

    return g.fig

