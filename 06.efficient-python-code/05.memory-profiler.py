# %load_ext memory_profiler
# %mprun -f fn_name fn_name(args)
# performance

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


# 1. Load the memory profiler extension in your IPython or Jupyter session:
#       %load_ext memory_profiler
#
# 2. Import the function you want to profile from its file.
#
#       from 05.memory-profiler.py import convert_units
#
# 3. Run the profiler on the convert_units() function:
#       %mprun -f convert_units convert_units(heroes, hts, wts)


# output:

# Filename: 05.memory-profiler.py, function convert_units
# Line #    Mem usage    Increment   Line Contents
# ==================================================
#      3     12.3 MiB     0.0 MiB   def convert_units(heroes, heights, weights):
#      4     12.3 MiB     0.1 MiB       new_hts = [ht * 0.39370 for ht in heights]
#      5     12.4 MiB     0.1 MiB       new_wts = [wt * 2.20462 for wt in weights]
#      6     12.4 MiB     0.0 MiB       hero_data = {}
#      7     12.4 MiB     0.0 MiB       for i, hero in enumerate(heroes):
#      8     12.4 MiB     0.1 MiB           hero_data[hero] = (new_hts[i], new_wts[i])
#      9     12.4 MiB     0.0 MiB       return hero_data
#
# Compare this to line_profiler, which focuses on execution time per line.
