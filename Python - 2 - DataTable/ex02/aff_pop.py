import seaborn as sns
from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def convert_population(population):
    """Convert population  to real numbers"""
    suffix = population[-1]
    value = float(population[:-1])
    if suffix == 'M':
        return value * 1e6
    elif suffix == 'k':
        return value * 1e3
    else:
        return value


def filter_country(country_df, years):
    """Filter the data for the desired year range"""
    start_year = 1800
    end_year = 2050
    selected_years = [
        col for col in years if start_year <= int(col) <= end_year]
    filtered_df = country_df[['country'] + selected_years].copy()
    # Convert population values to numeric
    for year in selected_years:
        filtered_df[year] = filtered_df[year].apply(convert_population)
    return filtered_df


def main():
    """Main function"""
    df = load("population_total.csv")
    france_df = df[df["country"] == "France"]
    belgium_df = df[df["country"] == "Belgium"]
    years = df.columns[1:]
    # Filter Country
    filtered_fr_df = filter_country(france_df, years)
    filtered_bel_df = filter_country(belgium_df, years)
    # Melt the DataFrames
    france_melted = pd.melt(filtered_fr_df, id_vars="country",
                            var_name="Year", value_name="Population")
    belgium_melted = pd.melt(filtered_bel_df, id_vars="country",
                             var_name="Year", value_name="Population")
    # retrieves the current Axes object using plt.gca().
    ax = plt.gca()
    # Create the Seaborn plot
    sns.lineplot(x="Year", y="Population", data=belgium_melted,
                 label="Belgium", color="blue")
    sns.lineplot(x="Year", y="Population", data=france_melted,
                 label="France", color="green")
    plt.title("Population Projections")
    plt.legend(loc="lower right")
    # Generates a range of values from 0 to 9 times 40 (360) with a step of 40.
    ax.set_xticks(range(0, 7 * 40, 40))
    plt.yticks([0, 20_000_000, 40_000_000, 60_000_000],
               ["", "20M", "40M", "60M"])
    plt.show()


if __name__ == "__main__":
    main()
