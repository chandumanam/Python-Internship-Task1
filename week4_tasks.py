import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

np.random.seed(42)
data = pd.DataFrame({
    "Age": np.random.randint(18, 60, 100),
    "Salary": np.random.randint(30000, 90000, 100),
    "Department": np.random.choice(["HR", "IT", "Finance", "Marketing"], 100),
    "Score": np.random.rand(100) * 100
})

print("Sample Dataset:\n", data.head())

plt.plot(data["Age"][:20], data["Salary"][:20], marker="o")
plt.title("Line Plot: Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()

plt.hist(data["Salary"], bins=10, color="skyblue", edgecolor="black")
plt.title("Histogram of Salary")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

plt.scatter(data["Age"], data["Score"], alpha=0.7, c="red")
plt.title("Scatter Plot: Age vs Score")
plt.xlabel("Age")
plt.ylabel("Score")
plt.show()

sns.boxplot(x="Department", y="Salary", data=data, palette="Set2")
plt.title("Boxplot: Department vs Salary")
plt.show()

plt.figure(figsize=(6,4))
sns.heatmap(data.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

sns.pairplot(data[["Age", "Salary", "Score"]], diag_kind="kde")
plt.suptitle("Pairplot of Features", y=1.02)
plt.show()

def create_dashboard(df):
    """Generate basic dashboard with scatter, histogram, and heatmap"""
    plt.figure(figsize=(10,5))
    
    plt.subplot(1,2,1)
    plt.scatter(df["Age"], df["Salary"], alpha=0.6, color="blue")
    plt.title("Age vs Salary")
    plt.xlabel("Age")
    plt.ylabel("Salary")
    
    plt.subplot(1,2,2)
    plt.hist(df["Score"], bins=8, color="green", edgecolor="black")
    plt.title("Distribution of Scores")
    plt.xlabel("Score")
    plt.ylabel("Frequency")
    
    plt.tight_layout()
    plt.show()

create_dashboard(data)
