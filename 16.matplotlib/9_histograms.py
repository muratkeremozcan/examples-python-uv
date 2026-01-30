import matplotlib.pyplot as plt
import numpy as np

# Key takeaways (histograms):
# - Histograms show distributions, not just averages.
# - ax.hist() plots the full variable; label + legend clarify groups.
# - bins controls the number or boundaries of bins.
# - histtype="step" avoids bars occluding each other.

rowing_heights = np.array([180, 182, 185, 188, 190, 192, 194, 186, 178, 181, 189, 193])
gym_heights = np.array([160, 162, 164, 166, 168, 170, 165, 163, 167, 169, 161, 171])

# Basic histogram comparison.
fig, ax = plt.subplots()
ax.hist(rowing_heights, label="Rowing", bins=6)
ax.hist(gym_heights, label="Gymnastics", bins=6)
ax.set_xlabel("Height (cm)")
ax.set_ylabel("Count")
ax.legend()
plt.show()

# Custom bins + step hist to reduce occlusion.
fig, ax = plt.subplots()
ax.hist(rowing_heights, bins=[160, 170, 180, 190, 200], histtype="step", label="Rowing")
ax.hist(
    gym_heights, bins=[160, 170, 180, 190, 200], histtype="step", label="Gymnastics"
)
ax.set_xlabel("Height (cm)")
ax.set_ylabel("Count")
ax.legend()
plt.show()
