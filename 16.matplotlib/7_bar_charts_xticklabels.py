import matplotlib.pyplot as plt
import pandas as pd

# Key takeaways (bar charts):
# Bar-charts show us the value of a variable in different conditions.
# - ax.bar creates a bar for each category.
# - Rotate tick labels when names are long.
# - Stacked bars use the bottom= argument.
# - Add labels + ax.legend() for clarity.

medals = pd.DataFrame(
    {
        "Gold": [46, 27, 17, 26],
        "Silver": [37, 23, 10, 18],
        "Bronze": [38, 17, 15, 26],
    },
    index=["USA", "Great Britain", "China", "Russia"],
)
print(medals)
#                Gold  Silver  Bronze
# USA              46      37      38
# Great Britain    27      23      17
# China            17      10      15
# Russia           26      18      26

fig, ax = plt.subplots()
ax.bar(medals.index, medals["Gold"], label="Gold")
ax.bar(
    medals.index,
    medals["Silver"],
    bottom=medals["Gold"],
    label="Silver",
)
ax.bar(
    medals.index,
    medals["Bronze"],
    bottom=medals["Gold"] + medals["Silver"],
    label="Bronze",
)
ax.set_ylabel("Medals")
ax.set_xticklabels(medals.index, rotation=90)
ax.legend()
plt.show()
