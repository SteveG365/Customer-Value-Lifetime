import numpy as np
import pandas as pd


# Functions for Engineering the features

def time_aggregate(df: pd.DataFrame):
    """
    A function that aggregates the data into unique timestamps
    """
    Invoice_Date = df["InvoiceDate"]
    df["Revenue"] = df['Price'] * df['Quantity']
    df["Date"]   = df["InvoiceDate"].dt.date
    df = (
    df
    .groupby("Date")
    .agg(
        revenue=("Revenue", "sum"),
        quantity=("Quantity", "sum"),
        customers=("Customer ID", "nunique")
    )
    .sort_index()
    .reset_index() #Makes sure that Date is now a column again and not an index (Still in order)
    )
    df["Date"] = pd.to_datetime(df["Date"])     #Convert back to datetime object
    df["Day"]    = df["Date"].dt.day
    df["Week"]   = df["Date"].dt.isocalendar().week
    df["Month"]  = df["Date"].dt.to_period("M")
    df["Weekday"]= df["Date"].dt.day_name()
    df["Is_Weekend"] = df["Weekday"].isin(["Friday", "Saturday", "Sunday"])

    return df



if __name__ == "__main__":
    pass