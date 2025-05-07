#Task2
import pandas as pd

def analyze_data(df):
    print("\nBasic statistics:")
    print(df.describe())
    
    print("\nMean by species:")
    print(df.groupby('species').mean())
    
    return df

if __name__ == "__main__":
    from data_loading import load_data
    df = load_data()
    analyze_data(df)
