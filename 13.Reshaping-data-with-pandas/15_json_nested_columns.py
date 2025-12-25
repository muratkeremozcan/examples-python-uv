import pandas as pd
import json

# Key takeaways: nested JSON columns
# - Method 1: json.loads -> apply(pd.Series) -> drop -> concat. (less steps)
# - Method 2 (alt): json.loads -> to_list -> json.dumps -> pd.read_json, then concat.

names = ['Killdeer', 'Chipping Sparrow', 'Cedar Waxwing']

bird_facts = ['{"Size" : "Large", "Color": "Golden brown", "Behavior": "Runs swiftly along ground", "Habitat": "Rocky areas"}', '{"Size":"Small", "Color": "Gray-white", "Behavior": "Often in flocks", "Habitat": "Open woodlands"}', '{"Size":"Small", "Color": "Gray-brown", "Behavior": "Catch insects over open water", "Habitat": "Parks"}']

# Define birds reading names and bird_facts lists into names and bird_facts columns 
birds = pd.DataFrame({'names': names, 'bird_facts': bird_facts})
# print(birds)
#               names                                         bird_facts
# 0          Killdeer  {"Size" : "Large", "Color": "Golden brown", "B...
# 1  Chipping Sparrow  {"Size":"Small", "Color": "Gray-white", "Behav...
# 2     Cedar Waxwing  {"Size":"Small", "Color": "Gray-brown", "Behav...

#######################

# Method 1: json.loads -> apply(pd.Series) -> drop -> concat.
 
# apply json.loads converts the json to a dictionary/object
# data_split = birds['bird_facts'].apply(json.loads)
# 0    {'Size': 'Large', 'Color': 'Golden brown', 'Be...
# 1    {'Size': 'Small', 'Color': 'Gray-white', 'Beha...
# 2    {'Size': 'Small', 'Color': 'Gray-brown', 'Beha...

# apply(pd.Series) converts the dictionary to a DataFrame
data_split = birds['bird_facts'].apply(json.loads).apply(pd.Series)
# print(data_split)
#     Size         Color                       Behavior         Habitat
# 0  Large  Golden brown      Runs swiftly along ground     Rocky areas
# 1  Small    Gray-white                Often in flocks  Open woodlands
# 2  Small    Gray-brown  Catch insects over open water           Parks

# Remove the original nested column before merging.
birds = birds.drop(columns=['bird_facts'])
# print(birds)
#              names
# 0          Killdeer
# 1  Chipping Sparrow
# 2     Cedar Waxwing

# Concatenate the flat columns with the expanded JSON columns.
birds = pd.concat([birds, data_split], axis=1)
print(birds)
#               names   Size         Color                       Behavior         Habitat
# 0          Killdeer  Large  Golden brown      Runs swiftly along ground     Rocky areas
# 1  Chipping Sparrow  Small    Gray-white                Often in flocks  Open woodlands
# 2     Cedar Waxwing  Small    Gray-brown  Catch insects over open water           Parks


###########################
# Method 2:  json.loads -> to_list -> json.dumps -> pd.read_json, then concat.
birds = pd.DataFrame({'names': names, 'bird_facts': bird_facts}) # reset birds

# Parse JSON strings to a list of dicts (array of objects).
birds_facts = birds['bird_facts'].apply(json.loads).to_list()
# print(birds_facts)	
# [{'Size': 'Large', 'Color': 'Golden brown', 'Behavior': 'Runs swiftly along ground', 'Habitat': 'Rocky areas'}, {'Size': 'Small', 'Color': 'Gray-white', 'Behavior': 'Often in flocks', 'Habitat': 'Open woodlands'}, {'Size': 'Small', 'Color': 'Gray-brown', 'Behavior': 'Catch insects over open water', 'Habitat': 'Parks'}]

# Serialize the list so pd.read_json can ingest it.
birds_dump = json.dumps(birds_facts)
# print(birds_dump)
# '[{"Size": "Large", "Color": "Golden brown", "Behavior": "Runs swiftly along ground", "Habitat": "Rocky areas"}, {"Size": "Small", "Color": "Gray-white", "Behavior": "Often in flocks", "Habitat": "Open woodlands"}, {"Size": "Small", "Color": "Gray-brown", "Behavior": "Catch insects over open water", "Habitat": "Parks"}]'	

# pd.read_json builds a DataFrame from the list-of-dicts JSON.
birds_df = pd.read_json(birds_dump)
# print(birds_df)
#     Size         Color                       Behavior         Habitat
# 0  Large  Golden brown      Runs swiftly along ground     Rocky areas
# 1  Small    Gray-white                Often in flocks  Open woodlands
# 2  Small    Gray-brown  Catch insects over open water           Parks

# Join the flat names with the expanded facts (same columns as Method 1).
birds_final = pd.concat([birds['names'], birds_df], axis=1)
# print(birds_final)
#               names   Size         Color                       Behavior         Habitat
# 0          Killdeer  Large  Golden brown      Runs swiftly along ground     Rocky areas
# 1  Chipping Sparrow  Small    Gray-white                Often in flocks  Open woodlands
# 2     Cedar Waxwing  Small    Gray-brown  Catch insects over open water           Parks
print(birds_final)