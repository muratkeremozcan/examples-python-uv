# 	Tuple unpacking and dictionary creation are powerful techniques in Python for organizing data.
# 	Converting structured data into a dictionary makes it more accessible.
# 	Sorting dictionaries by key allows structured outputs.
# Safe-access dictionaries with get()

squirrels = [
    ("Marcus Garvey Park", ("Black", "Cinnamon", "Cleaning", None)),
    (
        "Highbridge Park",
        ("Gray", "Cinnamon", "Running, Eating", "Runs From, watches us in short tree"),
    ),
    ("Madison Square Park", ("Gray", None, "Foraging", "Indifferent")),
    ("City Hall Park", ("Gray", "Cinnamon", "Eating", "Approaches")),
    ("J. Hood Wright Park", ("Gray", "White", "Running", "Indifferent")),
    ("Seward Park", ("Gray", "Cinnamon", "Eating", "Indifferent")),
    ("Union Square Park", ("Gray", "Black", "Climbing", None)),
    ("Tompkins Square Park", ("Gray", "Gray", "Lounging", "Approaches")),
]

squirrels_by_park = {}

for park, squirrel_details in squirrels:
    squirrels_by_park[park] = squirrel_details

print(squirrels_by_park)
# {
#     'Marcus Garvey Park': ('Black', 'Cinnamon', 'Cleaning', None),
#     'Highbridge Park': ('Gray', 'Cinnamon', 'Running, Eating', 'Runs From, watches us in short tree'),
#     'Madison Square Park': ('Gray', None, 'Foraging', 'Indifferent'),
#     'City Hall Park': ('Gray', 'Cinnamon', 'Eating', 'Approaches'),
#     'J. Hood Wright Park': ('Gray', 'White', 'Running', 'Indifferent'),
#     'Seward Park': ('Gray', 'Cinnamon', 'Eating', 'Indifferent'),
#     'Union Square Park': ('Gray', 'Black', 'Climbing', None),
#     'Tompkins Square Park': ('Gray', 'Gray', 'Lounging', 'Approaches')
# }


for park in sorted(squirrels_by_park):
    print(f"{park}: {squirrels_by_park[park]}")
# City Hall Park: ('Gray', 'Cinnamon', 'Eating', 'Approaches')
# Highbridge Park: ('Gray', 'Cinnamon', 'Running, Eating', 'Runs From, watches us in short tree')
# J.Hood Wright Park: ('Gray', 'White', 'Running', 'Indifferent')
# Madison Square Park: ('Gray', None, 'Foraging', 'Indifferent')
# Marcus Garvey Park: ('Black', 'Cinnamon', 'Cleaning', None)
# Seward Park: ('Gray', 'Cinnamon', 'Eating', 'Indifferent')
# Tompkins Square Park: ('Gray', 'Gray', 'Lounging', 'Approaches')
# Union Square Park: ('Gray', 'Black', 'Climbing', None)


#############
# safe-access with get(), the 2nd arg is the default return if nothing is
# found (otherwise things error)
print(squirrels_by_park.get("Union Square Park"))
print(type(squirrels_by_park.get("Fort Tryon Park")))
print(squirrels_by_park.get("Central Park", "Not Found"))


###########

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

squirrels_by_park["Madison Square Park"] = squirrels_madison

# Update squirrels_by_park with the squirrels_union[1] which is the list of squirrels
squirrels_by_park["Union Square Park"] = squirrels_union[1]

print(squirrels_by_park)
# {
#     'Marcus Garvey Park': ('Black', 'Cinnamon', 'Cleaning', None),
#     'Highbridge Park': ('Gray', 'Cinnamon', 'Running, Eating', 'Runs From, watches us in short tree'),
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
#     }],
#     'City Hall Park': ('Gray', 'Cinnamon', 'Eating', 'Approaches'),
#     'J. Hood Wright Park': ('Gray', 'White', 'Running', 'Indifferent'),
#     'Seward Park': ('Gray', 'Cinnamon', 'Eating', 'Indifferent'),
#     'Union Square Park': ('Union Square Park', [{
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
#     }]),
#     'Tompkins Square Park': ('Gray', 'Gray', 'Lounging', 'Approaches')
# }


# Loop over the park_name in the squirrels_by_park dictionary
for park_name in squirrels_by_park:
    # Safely print a list of the primary_fur_color for each squirrel in park_name
    if isinstance(squirrels_by_park[park_name], list):
        # For parks with list of dictionary values
        print(
            park_name,
            [
                squirrel.get("primary_fur_color", "N/A")
                for squirrel in squirrels_by_park[park_name]
            ],
        )
    else:
        # For parks with tuple values
        print(park_name, ["N/A"])
