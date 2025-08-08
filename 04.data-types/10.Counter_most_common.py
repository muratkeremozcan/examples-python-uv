from collections import Counter

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

# [output_if_true | for variable in iterable | if condition]
sexes = [penguin["sex"] for penguin in penguins]
print(sexes)

penguins_sex_counts = Counter(sexes)
print(penguins_sex_counts)

print(penguins_sex_counts.most_common())
print(penguins_sex_counts.most_common(1))
#########

penguins_species_counts = Counter([penguin["species"] for penguin in penguins])
print(penguins_species_counts)

print(penguins_species_counts.most_common())
print(penguins_species_counts.most_common(2))
