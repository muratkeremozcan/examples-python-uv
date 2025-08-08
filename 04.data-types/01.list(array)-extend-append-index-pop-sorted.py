baby_names = ["Ximena", "Aliza", "Ayden", "Calvin"]

# Use .extend() to add multiple elements at once
# This prevents nesting issues that would occur with .append()
baby_names.extend(["Rowen", "Sandeep"])
# JS equivalent:  babyNames.push(...['Rowen', 'Sandeep'])
# or:             babyNames.concat(['Rowen', 'Sandeep'])

position = baby_names.index("Rowen")
# JS equivalent:  babyNames.indexOf('Rowen')

# .pop() deletes and returns the value at the given index
baby_names.pop(position)
# JS equivalent:  babyNames.splice(position, 1)  # removes and returns the
# element at the given index

print(baby_names)
# JS equivalent: console.log(babyNames)

# with append, nesting can occur if we are passing an array
baby_names.append("Murat")
# JS equivalent: babyNames.push('Murat')
print(baby_names)
# JS equivalent: console.log(babyNames)

baby_names.append(["Kerem", "Ozcan"])
# JS equivalent: babyNames.push(['Kerem', 'Ozcan'])  # adds the array as a
# single element (nested array)
print(baby_names)


#########
# List comprehensions provide a concise way to transform lists.
# Use sorted() to return a new sorted list without modifying the original.

# List of lists (each entry contains: Year, Gender, Count, Name)
records = [
    ["2014", "F", "20799", "Emma"],
    ["2014", "M", "18656", "Noah"],
    ["2014", "F", "19674", "Olivia"],
    ["2014", "M", "18399", "Liam"],
]

# [output_if_true | for variable in iterable]
baby_names = [column[3] for column in records]
# JS equivalent: let babyNames = records.map(column => column[3])

# sorted(..) sorts in alphabetical order
print(sorted(baby_names))
# JS equivalent: console.log(babyNames.slice().sort())  // needs .slice to
# creates a new array
