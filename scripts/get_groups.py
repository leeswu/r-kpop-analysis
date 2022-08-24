import json
from mwclient import Site

# from Wikipedia listing of all K-Pop groups
site = Site('en.wikipedia.org')
category = site.categories["K-pop music groups"]
groups = []
# pull all groups into a list
for page in category:
    groups.append(page.name)
groups = groups[1:-2]  # remove headers

# clean up group names, remove (band)/(group) designations
for i in range(len(groups)):
    if " (" in groups[i]:
        groupPieces = groups[i].split(" (")[:-1]
        groups[i] = groups[i].join(groupPieces)
with open('../processed/groups_updated.json', 'w') as f:
    json.dump(groups, f, indent=2)

