import seaborn as sns
from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def main():
    # your tests and your error handling
    try:
        df = load("population_total.csv")
        france_df = df[df['country'] == 'France']
        # retrieves the current Axes object using plt.gca().
        ax = plt.gca()
        # Melt the DataFrame
        france_melted = pd.melt(
            france_df, id_vars='country',
            var_name='Year', value_name='Life Expectancy')
        # Create the Seaborn plot
        sns.lineplot(x='Year', y='Life Expectancy', data=france_melted)
        plt.title('France Life expectancy Projections')
        # Generates a range of values from 0 to 9 times 40 with a step of 40.
        ax.set_xticks(range(0, 9 * 40, 40))
        plt.show()
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    """Main function"""
    main()
