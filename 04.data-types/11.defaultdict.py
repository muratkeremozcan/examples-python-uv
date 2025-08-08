# defaultdict eliminates the need to manually check if a key exists before appending.
# useful for grouping data dynamically
from collections import defaultdict

weight_log = [
    ("Chinstrap", "FEMALE", 3800.0),
    ("Adlie", "FEMALE", 3450.0),
    ("Gentoo", "FEMALE", 4300.0),
    ("Adlie", "FEMALE", 3550.0),
    ("Adlie", "FEMALE", 3175.0),
    ("Gentoo", "MALE", 5400.0),
    ("Chinstrap", "MALE", 4500.0),
    ("Adlie", "MALE", 3900.0),
]

female_penguin_weights = {}

for species, sex, body_mass in weight_log:
    if sex == "FEMALE":
        # if species is already in the dictionary, create an empty list for any
        # missing species
        if species not in female_penguin_weights:
            female_penguin_weights[species] = []
        # Append the sex and body_mass as a tuple to the species keys list
        female_penguin_weights[species].append((sex, body_mass))

print(female_penguin_weights["Adlie"])

print(female_penguin_weights)
# {
#     'Chinstrap': [('FEMALE', 3800.0)],
#     'Adlie': [('FEMALE', 3450.0), ('FEMALE', 3550.0), ('FEMALE', 3175.0)],
#     'Gentoo': [('FEMALE', 4300.0)]
# }

# same thing with defaultdict

# defaultdict eliminates the need to manually check if a key exists before appending.
# defaultdict with a default type of list
female_penguin_weights = defaultdict(list)

for species, sex, body_mass in weight_log:
    if sex == "FEMALE":
        female_penguin_weights[species].append((sex, body_mass))


################

# vanilla

male_penguin_weights = {}

for species, sex, body_mass in weight_log:
    if sex == "MALE":
        # Check if species is already in the dictionary, if not, initialize with
        # an empty list
        if species not in male_penguin_weights:
            male_penguin_weights[species] = []

        # Append body_mass to the corresponding species list
        male_penguin_weights[species].append(body_mass)

print(male_penguin_weights)
# {
#     'Gentoo': [5400.0],
#     'Chinstrap': [4500.0],
#     'Adlie': [3900.0]
# }

# same thing with default dict

male_penguin_weights = defaultdict(list)

for species, sex, body_mass in weight_log:
    if sex == "MALE":
        # Use the species as the key, and append the body_mass to it
        male_penguin_weights[species].append(body_mass)


print(list(male_penguin_weights))
print(list(male_penguin_weights.items()))
print(list(male_penguin_weights.items())[:2])

#
