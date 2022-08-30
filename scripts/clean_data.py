import json

to_clean = ["Authors", "Link Flairs"]

def clean_counts(attribute, group):

    counts = []
    print(group[attribute])

    if attribute == "Authors":
        name = "Author"
    else:
        name = "Link Flair"

    for key, val in group[attribute].items():
        if key != 'null':
            counts.append({name : key, "Count": val})
    group[attribute] = counts    


with open("./processed_data/group_data_cleaned.json") as f:
    data = json.load(f)

for group in data.values():
    for attribute in to_clean:
        clean_counts(attribute, group)
    

with open('./processed_data/group_data_cleaned.json', 'w') as f:
    json.dump(data, f, indent=2)