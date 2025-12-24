import pandas as pd

def prepare_data(df):
    df['Revenue_Variance'] = df['Revenue'] - df['Budget_Revenue']
    df['Revenue_Variance_Pct'] = (df['Revenue_Variance'] / df['Budget_Revenue']) * 100
    df['Expenses_Variance'] = df['Expenses'] - df['Budget_Expenses']
    df['Expenses_Variance_Pct'] = (df['Expenses_Variance'] / df['Budget_Expenses']) * 100
    return df

def format_for_llm(df, rows=5):
    return df.head(rows).to_string(index=False)
