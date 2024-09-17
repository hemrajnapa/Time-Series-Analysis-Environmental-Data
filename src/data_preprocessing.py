import pandas as pd
import numpy as np

def load_data(filepath):
    """Loads the dataset from a CSV file"""
    return pd.read_csv(filepath)

def clean_data(df):
    """Preprocess the data by handling missing values and dropping unnecessary columns"""
    # Drop rows with null Rainfall_Bastia_Umbra and reset index
    df = df[df['Rainfall_Bastia_Umbra'].notna()].reset_index(drop=True)
    
    # Drop unwanted columns
    df = df.drop(['Depth_to_Groundwater_P24', 'Temperature_Petrignano'], axis=1)
    return df

def get_data_info(df):
    """Display dataset information"""
    return df.info()

if __name__ == "__main__":
    filepath = 'path_to_your_data.csv'
    df = load_data(filepath)
    df = clean_data(df)
    get_data_info(df)
