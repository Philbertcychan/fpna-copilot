import pandas as pd

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Revenue": [120000, 130000, 125000, 140000],
    "Expenses": [80000, 85000, 90000, 95000],
    "Budget_Revenue": [115000, 125000, 120000, 135000],
    "Budget_Expenses": [75000, 80000, 85000, 90000],
    "Department": ["Sales", "Sales", "Marketing", "Marketing"],
    "Notes": ["", "", "", ""]
}

df = pd.DataFrame(data)
df.to_csv("data/fake_fpna.csv", index=False)