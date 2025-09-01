
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/nfl_prop_lines.csv")

# Calculate hits
df["Hit"] = df["Actual"] > df["Line"]

# Summary
print("Hit Rate:", df["Hit"].mean())
print(df[["Player", "Line", "Actual", "Hit"]])

# Visualization
plt.figure(figsize=(8, 5))
plt.bar(df["Player"], df["Actual"], label="Actual", alpha=0.7)
plt.plot(df["Player"], df["Line"], label="Prop Line", linestyle='--', color="red", marker='o')
plt.title("NFL Player Prop Results vs. Lines")
plt.ylabel("Receiving Yards")
plt.xticks(rotation=15)
plt.legend()
plt.tight_layout()
plt.grid(True)
plt.show()
