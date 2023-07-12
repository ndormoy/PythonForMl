import seaborn as sns
from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


# def convert_number(nb):
#     """Convert nb  to real numbers"""
#     suffix = nb[-1]
#     value = float(nb[:-1])
#     if suffix == 'M':
#         return value * 1e6
#     elif suffix == 'k':
#         return value * 1e3
#     else:
#         return value


def main():
    try:
        
        income_df = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        life_expect_df = load("life_expectancy_years.csv")
        #filter the year to 1900
        life_expect_df = life_expect_df[["country", "1900"]]
        income_df = income_df[["country", "1900"]]
        # Step 3: Merge the DataFrames on country
        merged_df = income_df.merge(life_expect_df, on="country", how="outer")
        merged_df = merged_df.rename(columns={"1900_x": "Income", "1900_y": "life_expect"})
        print(merged_df)
        sns.scatterplot(x="Income", y="life_expect", data=merged_df)
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")
        plt.title("1900")
        # plt.xticks([0, 20_000_000, 40_000_000, 60_000_000],
        #         ["", "20M", "40M", "60M"])
        plt.show()




    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
    
