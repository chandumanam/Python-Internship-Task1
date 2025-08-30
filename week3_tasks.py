import numpy as np
import pandas as pd

arr = np.array([1, 2, 3, 4, 5])
print("NumPy Array:", arr)

print("Array + 10:", arr + 10)

print("Squares:", arr ** 2)
print("Sum of elements:", np.sum(arr))

matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("Matrix:\n", matrix)
print("Row sums:", matrix.sum(axis=1))
print("Column sums:", matrix.sum(axis=0))

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 35, np.nan, 28],
    "Salary": [50000, 60000, 75000, 80000, np.nan]
}
df = pd.DataFrame(data)
print("\nOriginal DataFrame:\n", df)

print("\nAges:", df["Age"])
print("First two rows:\n", df.head(2))

cleaned_df = df.dropna()
print("\nAfter removing missing values:\n", cleaned_df)

filled_df = df.fillna(df.mean(numeric_only=True))
print("\nAfter filling missing values:\n", filled_df)

grouped = filled_df.groupby("Age")["Salary"].mean()
print("\nAverage salary by age:\n", grouped)

def clean_and_aggregate(dataframe):
    """Remove missing values and calculate average salary by age"""
    cleaned = dataframe.dropna()
    result = cleaned.groupby("Age")["Salary"].mean()
    return result

print("\nClient Project - Cleaned & Aggregated:\n", clean_and_aggregate(df))
