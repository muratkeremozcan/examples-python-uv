import matplotlib.pyplot as plt
import numpy as np

# Key takeaways (summaries):
# - Use sum/min/max/mean to aggregate arrays.
# - axis=0 for rows, going down column s x axis=1 for columns going right
# - keepdims=True keeps collapsed dimensions for shape compatibility.
# - cumsum builds cumulative totals over time.

# (years, clients) / (rows, columns) / (5, 3)
breaches = np.array(
    [
        [2, 1, 0],
        [1, 3, 1],
        [0, 2, 2],
        [3, 4, 1],
        [1, 0, 2],
    ]
)

# Total breaches across all years and clients.
print(breaches.sum())  # 23

# Column totals (per client) and row totals (per year).
print(breaches.sum(axis=0))  # [ 7 10  6]

print(breaches.sum(axis=1))  # [ 3  5  2  8  3]

# Min/max/mean overall and by axis.
print(breaches.min(axis=0))  # [0 0 0]
print(breaches.max(axis=0))  # [3 4 2]

print(breaches.min(axis=1))  # [0 1 0 1 0]
print(breaches.max(axis=1))  # [2 3 4 4 2]

print(breaches.mean(axis=0))  # [1.4 2. 1.2]
print(breaches.mean(axis=1))  # [1.2 2. 0.4 2. 0.6]


# print(breaches.sum(axis=0)) # [ 7 10  6]
# keepdims preserves 2D shape.
print(breaches.sum(axis=0, keepdims=True))  # [[ 7 10  6]]


# cumsum for cumulative totals.
print(np.cumsum(breaches, axis=0))
# [[2 1 0]
#  [3 4 1]
#  [3 6 3]
#  [6 10 4]
#  [7 10 6]]

# Plot one client's cumulative breaches vs the mean.
cum_breaches = np.cumsum(breaches, axis=0)
client_1 = cum_breaches[:, 0]  # first column going down, adding up
# print(client_1) # [2 3 3 6 7] the first column
mean_cum = cum_breaches.mean(axis=1)
# print(mean_cum) # [1.2 2. 0.4 2. 0.6] the mean of each row

# simple plot
plt.plot(client_1, label="Client 1")  # only y given -> x defaults to 0..n-1
plt.plot(mean_cum, label="Mean (all clients)")  # only y given -> x defaults to 0..n-1
plt.xlabel("Year index")
plt.ylabel("Cumulative breaches")
plt.legend()
plt.show()

# Same plot, but explicit x and y (second arg is y-values).
# Build a 1..N x-axis to match the number of years in the data.
years = np.arange(1, len(client_1) + 1)  # # [1 2 3 4 5]
plt.plot(years, client_1, label="Client 1")  # x=years, y=client_1 (explicit axes)
plt.plot(years, mean_cum, label="Mean (all clients)")  # x=years, y=mean_cum
plt.xlabel("Year")
plt.ylabel("Cumulative breaches")
plt.legend()
plt.show()
