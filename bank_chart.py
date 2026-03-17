import pandas as pd

# Load the dataset
data = pd.read_csv("reviews_data.csv")

# Group data by bank and sentiment
summary = data.groupby(["bank", "sentiment"]).size().unstack(fill_value=0)

# Calculate total reviews
summary["total"] = summary["negative"] + summary["positive"]

# Calculate percentage of negative reviews
summary["negative_percentage"] = (
    summary["negative"] / summary["total"] * 100
)

# Print results
print("Summary of review sentiment per bank:")
print(summary)
