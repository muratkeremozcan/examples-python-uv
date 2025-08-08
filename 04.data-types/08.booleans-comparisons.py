# Empty lists, dictionaries, and other collections evaluate to False in boolean contexts.
# Use == for value comparison, and use "is" for identity comparison (checking if two objects share the same memory location).
# Use isclose when comparing numbers or floats


import math

my_list = []
print(bool(my_list))

my_list.append("cookies")
print(bool(my_list))


###############
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

for penguin in penguins:
    if penguin["body_mass"] > 3300:
        print(f"{penguin['species']} - {penguin['sex']}")

#########

penguin_305_details = {
    "species": "Adlie",
    "flipper_length": 190.0,
    "body_mass": 3050.0,
    "tracked": True,
    "sex": "FEMALE",
}


if penguin_305_details["sex"]:
    sex_is_true = penguin_305_details["sex"] is True
    print(f"{penguin_305_details['sex']}: {sex_is_true}")

if penguin_305_details["tracked"]:
    tracked_is_true = penguin_305_details["tracked"] is True
    print(f"{penguin_305_details['tracked']}: {tracked_is_true}")


######

a = 256
b = 256

print(a == b)  # ✅ True (Values are equal)
print(a is b)  # ✅ True (Same memory reference for small integers)

c = 257
d = 257

print(c == d)  # ✅ True (Values are equal)
print(c is d)  # ❌ False (Different memory locations)


x = 0.1 + 0.2
y = 0.3

print(x == y)  # ❌ False (Due to floating-point precision issues)
print(x is y)  # ❌ False (Different memory references)


# properly compare numbers or floats

print(math.isclose(x, y))
