import numpy as np
import pandas as pd


# Functions for Engineering the features

def time_aggregate(df: pd.DataFrame):
    """
    A function that aggregates the data into unique timestamps
    """

    df = df.sort_values("InvoiceDate")
    df["date"]   = df["InvoiceDate"].dt.date
    df["hour"]   = df["InvoiceDate"].dt.hour
    df["day"]    = df["InvoiceDate"].dt.day
    df["week"]   = df["InvoiceDate"].dt.isocalendar().week
    df["month"]  = df["InvoiceDate"].dt.to_period("M")
    df["weekday"]= df["InvoiceDate"].dt.day_name()

    df["Revenue"] = df['Price'] * df['Quantity']

    df = (
    df
    .groupby("date")
    .agg(
        revenue=("Revenue", "sum"),
        quantity=("Quantity", "sum"),
        customers=("Customer ID", "nunique")
    )
    .sort_index()
    )


    return df



if __name__ == "__main__":
    pass