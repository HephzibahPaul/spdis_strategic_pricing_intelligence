import pandas as pd
import os

def load_data(path=os.path.join("..","data","spdis_behavioral_data.csv")):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Data not found: {path}")
    return pd.read_csv(path)

def save_chart(fig, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fig.savefig(path, bbox_inches="tight")
