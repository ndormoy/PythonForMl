import seaborn as sns
from load_csv import load
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def main():
    try:
        income_df = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        life_expect_df = load("life_expectancy_years.csv")
        # filter the year to 1900
        life_expect_df = life_expect_df[["country", "1900"]]
        income_df = income_df[["country", "1900"]]
        # Step 3: Merge the DataFrames on country
        merged_df = income_df.merge(life_expect_df, on="country", how="outer")
        merged_df = merged_df.rename(
            columns={"1900_x": "Income", "1900_y": "life_expect"})
        print(merged_df)
        sns.scatterplot(x="Income", y="life_expect", data=merged_df)
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")
        plt.title("1900")
        plt.xscale('log')
        x_locator = ticker.FixedLocator([300, 1000, 10000])
        x_formatter = ticker.FixedFormatter(['300', '1k', '10k'])
        # Apply the custom locator and formatter to the x-axis
        plt.gca().xaxis.set_major_locator(x_locator)
        plt.gca().xaxis.set_major_formatter(x_formatter)
        plt.show()
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
