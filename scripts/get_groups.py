"""
Extracts a list of all K-Pop musical groups from the relevant Wikipedia Listing
"""

import json
from mwclient import Site

# From Wikipedia listing of all K-Pop groups
site = Site('en.wikipedia.org')
category = site.categories["K-pop music groups"]
groups = []

for page in category:
    groups.append(page.name)
groups = groups[1:-2]  # remove headers

# Clean up group names, remove (band)/(group) designations
for i in range(len(groups)):
    if " (" in groups[i]:
        groupPieces = groups[i].split(" (")[:-1]
        groups[i] = groups[i].join(groupPieces)

with open('../processed/groups_updated.json', 'w') as f:
    json.dump(groups, f, indent=2)

