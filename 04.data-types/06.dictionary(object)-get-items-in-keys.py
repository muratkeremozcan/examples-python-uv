# Using .items() for cleaner dictionary iteration instead of manual key lookup.
# Using .get() and .pop() when safe key access or removal is needed.
# Checking for key existence with `in`, replacing the need for .get() in some cases.
# Using .keys() returns a dynamic view of the dictionary's keys.

squirrels_by_park = {
    "Madison Square Park": [
        {
            "primary_fur_color": "Gray",
            "highlights_in_fur_color": None,
            "activities": "Foraging",
            "interactions_with_humans": "Indifferent",
        },
        {
            "primary_fur_color": "Gray",
            "highlights_in_fur_color": None,
            "activities": "Sitting",
            "interactions_with_humans": "Indifferent",
        },
    ],
    "Union Square Park": [
        {
            "primary_fur_color": "Gray",
            "highlights_in_fur_color": None,
            "activities": "Eating, Foraging",
            "interactions_with_humans": None,
        },
        {
            "primary_fur_color": "Cinnamon",
            "highlights_in_fur_color": None,
            "activities": "Foraging",
            "interactions_with_humans": None,
        },
        {
            "primary_fur_color": "Gray",
            "highlights_in_fur_color": None,
            "activities": "Eating, Foraging",
            "interactions_with_humans": None,
        },
        {
            "primary_fur_color": "Gray",
            "highlights_in_fur_color": None,
            "activities": "Digging",
            "interactions_with_humans": "Indifferent",
        },
    ],
    "Tompkins Square Park": [
        {
            "primary_fur_color": "Gray",
            "highlights_in_fur_color": "Gray",
            "activities": "Foraging",
            "interactions_with_humans": "Approaches",
        },
        {
            "primary_fur_color": "Gray",
            "highlights_in_fur_color": "Gray",
            "activities": "Climbing (down tree)",
            "interactions_with_humans": "Indifferent",
        },
        {
            "primary_fur_color": "Gray",
            "highlights_in_fur_color": "Gray",
            "interactions_with_humans": "Indifferent",
        },
        {
            "primary_fur_color": "Gray",
            "highlights_in_fur_color": "Gray",
            "activities": "Foraging",
            "interactions_with_humans": "Indifferent",
        },
    ],
}

# before using items() : manual key lookup
for park_name in squirrels_by_park:
    print(park_name, squirrels_by_park[park_name])


# after using .items() : direct key-value unpacking
for park_name, squirrel_list in squirrels_by_park.items():
    print(park_name, squirrel_list)

# .items() simplified
fruit_colors = {"apple": "red", "banana": "yellow", "grape": "purple"}
# console.log(Object.entries(fruitColors)) // JS version
# [['apple', 'red'], ['banana', 'yellow'], ['grape', 'purple']]
print(fruit_colors.items())

# Using .items() to iterate over key-value pairs
for fruit, color in fruit_colors.items():
    print(f"The color of {fruit} is {color}")

# #########

for field, value in squirrels_by_park["Madison Square Park"][0].items():
    print(field, value)

print("-" * 13)

# primary_fur_color Gray
# highlights_in_fur_color None
# activities Foraging
# interactions_with_humans Indifferent

# for field, value in squirrels_by_park['Union Square Park'][1].items():
# 	print(field, value)

# ########

# previously we were using get(key, default)  and pop(key, default) to get the value of a key
# checking for key existence with `in`, replaces the need for .get() in some cases.

# in is used to check if a key exists
if squirrels_by_park.get("Tompkins Square Park") is not None:
    print("Found Tompkins Square Park")

if "Tompkins Square Park" in squirrels_by_park:
    print("Found Tompkins Square Park")


if squirrels_by_park.get("Central Park") is not None:
    print("Found Central Park")
else:
    print("Central Park missing")


if "Central Park" in squirrels_by_park:
    print("Found Central Park")
else:
    print("Central Park missing")


# ########

print(squirrels_by_park.keys())
# console.log(Object.keys(fruitColors)) JS equivalent

# regular access gets keys and values
print(squirrels_by_park["Union Square Park"][0])
# .keys() gets only the keys
print(squirrels_by_park["Union Square Park"][0].keys())

for park_name in squirrels_by_park:
    squirrel_data = squirrels_by_park[park_name][0]
    print()
    print(park_name, squirrel_data.get("highlights_in_fur_color", "N/A"))


# ###############
# print('-' * 13)

# # Use a for loop to iterate over the squirrels in Tompkins Square Park:
for squirrel in squirrels_by_park["Tompkins Square Park"]:
    # Safely print the activities of each squirrel or 'None' (default 2nd arg is None)
    print(squirrel.get("activities"))

# print('-' * 13)

# # Print the list of 'Cinnamon' primary_fur_color squirrels in Union Square Park
# # [output_if_true | for variable in iterable | if condition]
# print([squirrel for squirrel in squirrels_by_park['Union Square Park'] if squirrel.get('primary_fur_color') == 'Cinnamon'])
