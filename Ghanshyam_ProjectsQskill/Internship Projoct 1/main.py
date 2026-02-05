import pandas as pd
import matplotlib
matplotlib.use("Agg")   
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV
df = pd.read_csv("data\Data.csv")

# Drop unwanted column
if "Unnamed: 0" in df.columns:
    df.drop(columns=["Unnamed: 0"], inplace=True)

# Numeric columns
numeric_df = df.select_dtypes(include="number")

# Average
average_scores = numeric_df.mean()
print("Average Scores:")
print(average_scores)

# -------- Bar Chart --------
average_scores.plot(kind="bar")
plt.title("Average Student Scores")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.savefig("average_scores.png")
plt.close()

# -------- Scatter Plot --------
plt.scatter(df["math.score"], df["reading.score"])
plt.xlabel("Math Score")
plt.ylabel("Reading Score")
plt.title("Math vs Reading Scores")
plt.savefig("math_vs_reading.png")
plt.close()

# -------- Heatmap --------
sns.heatmap(numeric_df.corr(), annot=True)
plt.title("Correlation Heatmap")
plt.savefig("correlation_heatmap.png")
plt.close()

print("Graphs saved successfully!")
