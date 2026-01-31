import matplotlib.pyplot as plt
import seaborn as sns

# Key takeaways (Seaborn intro):
# - Seaborn is a higher-level interface to Matplotlib.
# - Makes common plots easier at the cost of less flexibility.

# Sample data.
heights = [62, 65, 68, 70, 72, 64, 66, 69, 71, 73]
weights = [120, 130, 150, 160, 175, 125, 135, 155, 165, 180]
gender = [
    "Female",
    "Male",
    "Male",
    "Male",
    "Male",
    "Female",
    "Female",
    "Male",
    "Male",
    "Female",
]

# Example 1: scatter plot.
sns.scatterplot(x=heights, y=weights)
plt.show()

# Example 2: count plot.
sns.countplot(x=gender)
plt.show()

# Matplotlib comparison (same data, more manual setup).
plt.scatter(heights, weights)
plt.xlabel("Height (in)")
plt.ylabel("Weight (lb)")
plt.show()

counts = {"Male": gender.count("Male"), "Female": gender.count("Female")}
plt.bar(counts.keys(), counts.values())
plt.show()
