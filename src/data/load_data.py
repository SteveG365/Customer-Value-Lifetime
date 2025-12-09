import argparse
import numpy as np
import pandas as pd

def load_cd():
    data = pd.read_csv("../../data/CDNOW_master.txt", 
                       header=None, 
                       sep=r"\s+",
                       names=["customer_id", "date", "num_cds", "amount"], 
                       index_col=False)
    
    data['date'] = pd.to_datetime(data['date'], format="%Y%m%d")
    #data.to_csv("../../data/CD_data.csv", index=False)
    return data

def load_online(path):
    data = pd.read_excel(path)
    return data


if __name__ == "__main__":
    """
    How to run:
    python load_data.py --dataset <name>
    where <name> can either be "CDNOW" or "online_retail_2"
    """
    parser = argparse.ArgumentParser(description="Generate QST dataset")
    parser.add_argument('--dataset', type=str)

    args = parser.parse_args()

    name = args.dataset

    if (name != "CDNOW" or name != "online_retail_2"):
        print("Dataset does not exist, must use either CDNOW or online_retail_2")
    
    match name:
        case "CDNOW":
            load_cd()
        case "online_retail_2":
            load_online()