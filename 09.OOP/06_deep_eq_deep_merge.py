# DeepDiff: For deep comparison of complex objects (nested dicts, lists, etc.)
# always_merger: For deep merging dictionaries, handling nested structures automatically

from deepdiff import DeepDiff

dict1 = {"a": 1, "b": {"c": 2}}
dict2 = {"a": 1, "b": {"c": 2}}

# Check if objects are equal
diff = DeepDiff(dict1, dict2)
if not diff:
    print("Objects are equal")


# For direct boolean comparison
def deep_equal(a, b):
    return not DeepDiff(a, b)


print(deep_equal(dict1, dict2))  # True


#########

from deepmerge import always_merger

dict1 = {"a": 1, "b": {"x": 10, "y": 20}}
dict2 = {"b": {"y": 30, "z": 40}, "c": 3}

# Deep merge dictionaries
merged = always_merger.merge(dict1, dict2)
print(merged)
