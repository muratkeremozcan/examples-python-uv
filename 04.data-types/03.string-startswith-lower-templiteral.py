top_ten_girl_names = [
    (1, "Jada"),
    (2, "Emily"),
    (3, "Ava"),
    (4, "Serenity"),
    (5, "Claire"),
    (6, "Sophia"),
    (7, "Sarah"),
    (8, "Ashley"),
    (9, "Chaya"),
    (10, "Abigail"),
]

# Looping through the list and unpacking each tuple
for top_ten_rank, name in top_ten_girl_names:
    print(f"Rank #: {top_ten_rank} - {name}")


##############

boy_names = [
    "Josiah",
    "Ethan",
    "David",
    "Jayden",
    "Mason",
    "Ryan",
    "Christian",
    "Isaiah",
    "Jayden",
    "Michael",
]

preamble = "The top ten boy names are: "
conjunction = ", and"

first_nine_names = ", ".join(boy_names[0:9])
print(first_nine_names)

print(f"{preamble}{first_nine_names}{conjunction} {boy_names[-1]}.")

#######

girl_names = [
    "Jada",
    "Emily",
    "Ava",
    "Serenity",
    "Claire",
    "Sophia",
    "Sarah",
    "Ashley",
    "Chaya",
    "Abigail",
    "Zoe",
    "Leah",
    "Hailey",
    "Ava",
    "Olivia",
    "Emma",
    "Chloe",
    "Sophia",
    "Aaliyah",
    "Angela",
    "Camila",
    "Savannah",
    "Serenity",
    "Fatoumata",
]

names_with_s = [name for name in girl_names if name.lower().startswith("s")]
print(names_with_s)

# [output_if_true | for variable in iterable | if condition]
names_with_angel = [name for name in girl_names if "angel" in name.lower()]
print(names_with_angel)
