# A numpy array contains homogeneous data types (which reduces memory consumption)
# numpy provides the ability to apply operations on all elements

import numpy as np

nums = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(nums, "\n")
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]]

# Print second row of nums
print(nums[1, :], "\n")
# [ 6  7  8  9 10]

# Print all elements of nums that are greater than six
print(nums[nums > 6], "\n")
# [ 7  8  9 10]

# numpy provides the ability to apply operations on all elements
nums_dbl = nums * 2
print(nums_dbl, "\n")
# [[ 2  4  6  8 10]
#  [12 14 16 18 20]]

# Replace the third column of nums
nums[:, 2] = nums[:, 2] + 1
print(nums, "\n--------------")
# [[ 1  2  4  4  5]
#  [ 6  7  9  9 10]]

####################
names = ["Jerry", "Kramer", "Elaine", "George", "Newman"]
arrival_times = [*range(10, 60, 10)]

print(arrival_times, "\n")
# [10, 20, 30, 40, 50]

# Convert arrival_times to an array and update the times
arrival_times_np = np.array(arrival_times)
new_times = arrival_times_np - 3
print(new_times, "\n")
# [ 7 17 27 37 47]
print(*enumerate(new_times), "\n")
# (0, 7) (1, 17) (2, 27) (3, 37) (4, 47)

# Use list comprehension and enumerate to pair guests to new times
# [output_if_true | for variable in iterable | if condition]
guest_arrivals = [(names[i], time) for i, time in enumerate(new_times)]
print(guest_arrivals, "\n")
# [('Jerry', 7), ('Kramer', 17), ('Elaine', 27), ('George', 37), ('Newman', 47)]


def welcome_guest(guest):
    name, time = guest
    return f"Welcome {name}! You arrived {time} minutes late."


# Map the welcome_guest function to each (guest,time) pair
welcome_map = map(welcome_guest, guest_arrivals)

guest_welcomes = [*welcome_map]
print(guest_welcomes)
# ['Welcome Jerry! You arrived 7 minutes late.', 'Welcome Kramer! You arrived 17 minutes late.', 'Welcome Elaine! You arrived 27 minutes late.', 'Welcome George! You arrived 37 minutes late.', 'Welcome Newman! You arrived 47 minutes late.']

print(*guest_welcomes, sep="n")
# Welcome Jerry! You arrived 7 minutes late.nWelcome Kramer! You arrived 17 minutes late.nWelcome Elaine! You arrived 27 minutes late.nWelcome George! You arrived 37 minutes late.nWelcome Newman! You arrived 47 minutes late.
