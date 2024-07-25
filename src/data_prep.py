import pandas as pd
import numpy as np
import os

train_data  = pd.read_csv(r'C:\Users\espym.LAPTOP-41F90NSA\projects\ml_pipeline\data\raw\train.csv')
test_data = pd.read_csv(r'C:\Users\espym.LAPTOP-41F90NSA\projects\ml_pipeline\data\raw\test.csv')

def fill_null_with_median(df):
    for col in df.columns:
        if df[col].isnull().any():
            median_val = df[col].median()
            df[col].fillna(median_val, inplace=True)
    return df

train_processed = fill_null_with_median(train_data)
test_processed = fill_null_with_median(test_data)

data_path = os.path.join("data", "processed")

os.makedirs(data_path)

train_processed.to_csv(os.path.join(data_path, "train_processed.csv"),index=False)
test_processed.to_csv(os.path.join(data_path, "test_processed.csv"),index=False)
