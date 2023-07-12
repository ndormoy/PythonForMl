import pandas as pd
import os


def load(path: str) -> pd.DataFrame:
    try:
        if not isinstance(path, str):
            return None
        elif not os.path.exists(path):
            return None
        elif not path.lower().endswith('.csv'):
            return None
        # Load the data into a DataFrame
        df = pd.read_csv(path)
        print("Loading dataset of dimension", str(df.shape))
    except AssertionError as e:
        print(e)
    return df
