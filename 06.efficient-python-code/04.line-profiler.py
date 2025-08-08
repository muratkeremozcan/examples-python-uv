# %load_ext line_profiler
# %lprun -f fn-name fn-name(args)
# performance

# using %timeit in multi-line code is inefficient, so we use code-profiling
import numpy as np


def convert_units(heroes, heights, weights):

    new_hts = [ht * 0.39370 for ht in heights]
    new_wts = [wt * 2.20462 for wt in weights]

    hero_data = {}

    for i, hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])

    return hero_data


heroes = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman"]
hts = np.array([191, 183, 182, 175, 188])
wts = np.array([107, 95, 75, 70, 90])

# 1. Load the line profiler extension in your IPython or Jupyter session:
#       %load_ext line_profiler
#
# 2. Run the profiler on the convert_units() function:
#      %lprun -f convert_units convert_units(heroes, hts, wts)


# output:
# Timer unit: 1e-06 s

# Total time: 32 µs
# File: <ipython-input-1>, function convert_units
# Line #      Hits         Time  Per Hit   % Time  Line Contents
# ==============================================================
#      3                                           def convert_units(heroes, heights, weights):
#      4         1         7 µs      7 µs    21.88      new_hts = [ht * 0.39370 for ht in heights]
#      5         1         8 µs      8 µs    25.00      new_wts = [wt * 2.20462 for wt in weights]
#      6         1         4 µs      4 µs    12.50      hero_data = {}
#      7         1         7 µs      7 µs    21.88      for i, hero in enumerate(heroes):
#      8         1         6 µs      6 µs    18.75          hero_data[hero] = (new_hts[i], new_wts[i])
#      9         1         0 µs      0 µs     0.00      return hero_data
