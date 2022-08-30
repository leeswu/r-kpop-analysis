"""
Takes the raw collections of all posts and organizes by which K-Pop groups are mentioned in the title.
Also extracts important counts of certain attributes.
"""

import json
from collections import Counter

def addData(group, group_data, post):
    group_data[group]["Authors"].append(post["Author"])
    group_data[group]["Created"].append(post["Time Created"])
    group_data[group]["Distinguished"].append(post["Distinguished"])
    group_data[group]["Edited"].append(post["Edited"])
    group_data[group]["Link Flairs"].append(post["Link Flair Text"])
    group_data[group]["Locked"].append(post["Locked"])
    group_data[group]["NSFW"].append(post["NSFW"])
    group_data[group]["Num Comments"].append(post["Num Comments"])
    group_data[group]["Num Posts"] += 1
    group_data[group]["Original"].append(post["Is Original"])
    group_data[group]["Scores"].append(post["Score"])
    group_data[group]["Self"].append(post["Is Self"])
    group_data[group]["Spoiler"].append(post["Spoiler"])
    group_data[group]["Stickied"].append(post["Stickied"])
    group_data[group]["Upvote Ratios"].append(post["Upvote Ratio"])

# Import the complete set of posts
with open("./raw_data/all_posts_complete.json") as f:
    all_posts = json.load(f)

# Import the list of all K-Pop musical groups
with open("./processed_data/groups_updated.json") as f:
    groups = json.load(f)

# Initialize the dict
group_data = {group: 
    {
        "Name": group,
        "Authors": [],
        "Created": [],
        "Distinguished": [],
        "Edited": [],
        "Link Flairs": [],
        "Locked": [],
        "NSFW": [],
        "Num Comments": [],
        "Num Posts": 0,
        "Original": [],
        "Scores": [], 
        "Self": [],
        "Spoiler": [],
        "Stickied": [],
        "Upvote Ratios": []
    } for group in groups}

for title, data in all_posts.items():
    title = title.casefold()

    for group in groups:
        if "[" in group:
            # Account for "alternative" names/abbreviations for groups
            # Ex. TXT for Tomorrow X Together
            alt_group = group[group.find('[')+1:group.find(']')]

            # Add data under "official" grouop name
            if alt_group.casefold() in title or group.casefold() in title:
                addData(group, group_data, data)
        else:
            if group.casefold() in title:
                addData(group, group_data, data)

# Extract counts from raw data
for group, data in group_data.items():
    data["Authors"] = Counter(data["Authors"])
    data["Distinguished"] = Counter(data["Distinguished"])["moderator"]
    data["Edited"] = Counter(data["Edited"])[True]
    data["Link Flairs"] = Counter(data["Link Flairs"])
    data["Locked"] = Counter(data["Locked"])[True]
    data["NSFW"] = Counter(data["NSFW"])[True]
    data["Original"] = Counter(data["Original"])[True]
    data["Self"] = Counter(data["Self"])[True]
    data["Spoiler"] = Counter(data["Spoiler"])[True]
    data["Stickied"] = Counter(data["Stickied"])[True]


with open('./processed_data/group_data_complete.json', 'w') as f:
    json.dump(group_data, f, indent=2)