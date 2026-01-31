from io import StringIO

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Key takeaways (pandas + Seaborn):
# - Seaborn works well with pandas DataFrames by referencing column names.
# - Count plots need tidy data: one row per observation, one column per variable.
# - When x/y is a DataFrame column name, Seaborn auto-labels the axis.

# Reproducible mini-dataset (CSV string -> DataFrame).
csv_text = """participant_id,age,how_masculine,how_important
1,24,somewhat,very
2,31,very,very
3,27,somewhat,quite
4,45,not at all,not at all
5,38,somewhat,very
6,29,very,quite
7,52,not very,quite
8,34,somewhat,very
"""

df = pd.read_csv(StringIO(csv_text))
# print(df)
#    participant_id  age how_masculine how_important
# 0               1   24      somewhat          very
# 1               2   31          very          very
# 2               3   27      somewhat         quite
# 3               4   45    not at all    not at all
# 4               5   38      somewhat          very
# 5               6   29          very         quite
# 6               7   52      not very         quite
# 7               8   34      somewhat          very


# Count plot using a DataFrame column.
sns.countplot(x="how_masculine", data=df)
plt.title("How masculine do you feel?")
plt.show()


# Matplotlib comparison (manual counts + bar chart).
counts = df["how_masculine"].value_counts()
plt.bar(counts.index, counts.values)
plt.title("How masculine do you feel? (Matplotlib)")
plt.xlabel("how_masculine")
plt.ylabel("count")
plt.show()
