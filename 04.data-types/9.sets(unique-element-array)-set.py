# set's difference with list/array: unique elements, no index access
# Use set() to convert lists into sets for uniqueness.
# difference() finds elements in one set but not in another.
# union() merges sets, keeping unique values.
# intersection() finds common elements between sets.
# len(set) returns the number of unique elements.

penguins = [
    {"species": "Adlie", "flipper_length": 190.0, "body_mass": 3050.0, "sex": "FEMALE"},
    {"species": "Adlie", "flipper_length": 184.0, "body_mass": 3325.0, "sex": "FEMALE"},
    {
        "species": "Gentoo",
        "flipper_length": 209.0,
        "body_mass": 4800.0,
        "sex": "FEMALE",
    },
    {"species": "Adlie", "flipper_length": 193.0, "body_mass": 4200.0, "sex": "MALE"},
    {
        "species": "Gentoo",
        "flipper_length": 210.0,
        "body_mass": 4400.0,
        "sex": "FEMALE",
    },
    {
        "species": "Gentoo",
        "flipper_length": 213.0,
        "body_mass": 4650.0,
        "sex": "FEMALE",
    },
    {
        "species": "Chinstrap",
        "flipper_length": 193.0,
        "body_mass": 3600.0,
        "sex": "FEMALE",
    },
    {"species": "Adlie", "flipper_length": 193.0, "body_mass": 3800.0, "sex": "MALE"},
    {
        "species": "Chinstrap",
        "flipper_length": 199.0,
        "body_mass": 3900.0,
        "sex": "FEMALE",
    },
    {
        "species": "Chinstrap",
        "flipper_length": 195.0,
        "body_mass": 3650.0,
        "sex": "FEMALE",
    },
    {"species": "Adlie", "flipper_length": 185.0, "body_mass": 3700.0, "sex": "FEMALE"},
    {
        "species": "Gentoo",
        "flipper_length": 208.0,
        "body_mass": 4575.0,
        "sex": "FEMALE",
    },
    {"species": "Adlie", "flipper_length": 196.0, "body_mass": 4350.0, "sex": "MALE"},
    {"species": "Adlie", "flipper_length": 191.0, "body_mass": 3700.0, "sex": "FEMALE"},
    {
        "species": "Chinstrap",
        "flipper_length": 195.0,
        "body_mass": 3300.0,
        "sex": "FEMALE",
    },
    {"species": "Adlie", "flipper_length": 195.0, "body_mass": 3450.0, "sex": "FEMALE"},
    {"species": "Gentoo", "flipper_length": 217.0, "body_mass": 4875.0, "sex": "."},
    {
        "species": "Gentoo",
        "flipper_length": 212.0,
        "body_mass": 4875.0,
        "sex": "FEMALE",
    },
    {"species": "Adlie", "flipper_length": 205.0, "body_mass": 4300.0, "sex": "MALE"},
    {"species": "Gentoo", "flipper_length": 220.0, "body_mass": 6000.0, "sex": "MALE"},
]
male_penguin_species = {"Gentoo", "Adlie"}

# [output_if_true | for variable in iterable | if condition]
female_species_list = [
    penguin["species"] for penguin in penguins if penguin["sex"] == "FEMALE"
]  # ?

# set(..) converts an array to a set
female_penguin_species = set(female_species_list)  # ?

# set1.difference(set2) will show the delta
differences = female_penguin_species.difference(male_penguin_species)  # ?

# set1.union(set2) combines them
all_species = female_penguin_species.union(male_penguin_species)  # ?

# set1.intersection(set2) wills show the intersection
overlapping_species = female_penguin_species.intersection(male_penguin_species)  # ?

# len(set1) gets the length, same as the array/list method
print(len(all_species))
len(penguins)  # ?


############
# JS equivalent would take some work

# const setA = new Set([1, 2, 3]);
# const setB = new Set([3, 4, 5]);

# // Union: combine both sets into a new one.
# const union = new Set([...setA, ...setB]);
# console.log(union); // Set { 1, 2, 3, 4, 5 }

# // Intersection: filter setA for elements that exist in setB.
# const intersection = new Set([...setA].filter(x => setB.has(x)));
# console.log(intersection); // Set { 3 }

# // Difference: elements in setA that are not in setB.
# const difference = new Set([...setA].filter(x => !setB.has(x)));
# console.log(difference); // Set { 1, 2 }
