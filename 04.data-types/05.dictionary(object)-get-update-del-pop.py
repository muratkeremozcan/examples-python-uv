# update() can add or modify dictionary entries when provided with a list of key-value tuples, e.g., dictionary.update([('key', value)]).
# List comprehension extracts values efficiently, like [squirrel.get('primary_fur_color', 'N/A') for squirrel in squirrels_by_park[key]].
# pop() safely removes dictionary entries, returning a default value (2nd arg) if the key doesn’t exist, similar to get().
# del permanently removes keys, but raises an error if the key is missing, unlike pop().

# Initial dictionary with empty list for Union Square Park
squirrels_by_park = {"Union Square Park": []}

# Madison Square Park squirrels data
squirrels_madison = [
    {
        "primary_fur_color": "Gray",
        "highlights_in_fur_color": None,
        "activities": "Sitting",
        "interactions_with_humans": "Indifferent",
    },
    {
        "primary_fur_color": "Gray",
        "highlights_in_fur_color": "Cinnamon",
        "activities": "Foraging",
        "interactions_with_humans": "Indifferent",
    },
    {
        "primary_fur_color": "Gray",
        "highlights_in_fur_color": None,
        "activities": "Climbing, Foraging",
        "interactions_with_humans": "Indifferent",
    },
]

# Union Square Park squirrels data
squirrels_union = (
    "Union Square Park",
    [
        {
            "primary_fur_color": "Gray",
            "highlights_in_fur_color": None,
            "activities": "Eating, Foraging",
            "interactions_with_humans": None,
        },
        {
            "primary_fur_color": "Gray",
            "highlights_in_fur_color": "Cinnamon",
            "activities": "Climbing, Eating",
            "interactions_with_humans": None,
        },
        {
            "primary_fur_color": "Cinnamon",
            "highlights_in_fur_color": None,
            "activities": "Foraging",
            "interactions_with_humans": "Indifferent",
        },
        {
            "primary_fur_color": "Gray",
            "highlights_in_fur_color": None,
            "activities": "Running, Digging",
            "interactions_with_humans": "Runs From",
        },
        {
            "primary_fur_color": "Gray",
            "highlights_in_fur_color": None,
            "activities": "Digging",
            "interactions_with_humans": "Indifferent",
        },
        {
            "primary_fur_color": "Gray",
            "highlights_in_fur_color": "Black",
            "activities": "Climbing",
            "interactions_with_humans": None,
        },
        {
            "primary_fur_color": "Gray",
            "highlights_in_fur_color": None,
            "activities": "Eating, Foraging",
            "interactions_with_humans": None,
        },
    ],
)

# Direct assignment for Madison Square Park:
squirrels_by_park["Madison Square Park"] = squirrels_madison
# at this point {'Union Square Park': [], 'Madison Square Park': [....] }
print(squirrels_by_park)

# update() method is used with a list containing the squirrels_union tuple: squirrels_by_park.update([squirrels_union])
# update() method expects a list of (key, value) tuples, and squirrels_union is already in this format.
# object.update(object)
# dictionary.update([('key', value)])
# Object.assign(object, Object.fromEntries([["key", value]]));
squirrels_by_park.update([squirrels_union])
print(squirrels_by_park)

# The loop then iterates through the dictionary keys and uses list comprehension to extract the
# 'primary_fur_color' from each squirrel dictionary, using get() to safely handle missing keys.
for park_name in squirrels_by_park:
    # [output_if_true | for variable in iterable]
    print(
        park_name,
        [
            squirrel.get("primary_fur_color", "N/A")
            for squirrel in squirrels_by_park[park_name]
        ],
    )

# pop() : like Js array.pop(), removes data and saves it off
squirrels_madison = squirrels_by_park.pop("Madison Square Park")

print(squirrels_madison)
print(squirrels_by_park)

# pop(arg, {}) : safe-delete with pop(), the 2nd arg is the default return
# if nothing is found (otherwise things error) - just like get
squirrels_city_hall = squirrels_by_park.pop("City Hall Park", {})
print(squirrels_city_hall)

# del is like del object['key'] in js; no safe delete (it will throw
# KeyError if the key doesn't exist)
del squirrels_by_park["Union Square Park"]
print(squirrels_by_park)


# squirrels_by_park
# {
#     'Union Square Park': [{
#         'primary_fur_color': 'Gray',
#         'highlights_in_fur_color': None,
#         'activities': 'Eating, Foraging',
#         'interactions_with_humans': None
#     }, {
#         'primary_fur_color': 'Gray',
#         'highlights_in_fur_color': 'Cinnamon',
#         'activities': 'Climbing, Eating',
#         'interactions_with_humans': None
#     }, {
#         'primary_fur_color': 'Cinnamon',
#         'highlights_in_fur_color': None,
#         'activities': 'Foraging',
#         'interactions_with_humans': 'Indifferent'
#     }, {
#         'primary_fur_color': 'Gray',
#         'highlights_in_fur_color': None,
#         'activities': 'Running, Digging',
#         'interactions_with_humans': 'Runs From'
#     }, {
#         'primary_fur_color': 'Gray',
#         'highlights_in_fur_color': None,
#         'activities': 'Digging',
#         'interactions_with_humans': 'Indifferent'
#     }, {
#         'primary_fur_color': 'Gray',
#         'highlights_in_fur_color': 'Black',
#         'activities': 'Climbing',
#         'interactions_with_humans': None
#     }, {
#         'primary_fur_color': 'Gray',
#         'highlights_in_fur_color': None,
#         'activities': 'Eating, Foraging',
#         'interactions_with_humans': None
#     }],
#     'Madison Square Park': [{
#         'primary_fur_color': 'Gray',
#         'highlights_in_fur_color': None,
#         'activities': 'Sitting',
#         'interactions_with_humans': 'Indifferent'
#     }, {
#         'primary_fur_color': 'Gray',
#         'highlights_in_fur_color': 'Cinnamon',
#         'activities': 'Foraging',
#         'interactions_with_humans': 'Indifferent'
#     }, {
#         'primary_fur_color': 'Gray',
#         'highlights_in_fur_color': None,
#         'activities': 'Climbing, Foraging',
#         'interactions_with_humans': 'Indifferent'
#     }]
# }
