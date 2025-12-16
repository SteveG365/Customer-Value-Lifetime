import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    
    # handle null values
    df = df.loc[~df['Customer ID'].isna()]

    return df

