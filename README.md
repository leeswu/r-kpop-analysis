# r/kpop Analysis

Gathering and processing post data taken from the subreddit [r/kpop](https://www.reddit.com/r/kpop/).

## Overview

In the K-Pop community, there is constant debate between fans about the popularity of their favorite groups. Which are more popular? Less? Who gets talked about the most? How are they perceived by the those in the community at large?

This multi-part project attempts to answer some of these questions by organizing and analyzing data from one of the largest gathering places of the K-Pop community on the internet: the subreddit r/kpop, home to over 1.7 million members.

By downloading and parsing every post from the subreddit's inception to July 1st, 2022, certain trends in who K-Pop fans are talking about and how well it is being received begin to emerge. The end goal is then to take these trends and visualize them in a way that is interesting and easily accessible in an interactive web app.

This repository focuses solely on the data gathering and cleaning portion of this project. The logic for the web app is contained separately

## 📁 Processed Data

### group_data_complete.json
Using the raw collection of all posts from r/kpop, organizes counts and statistics (number of submissions, the upvote ratio for those submissions, etc.) for each K-Pop music group. This is done by checking if a group's name is mentioned in the title of a post.

### groups_updated.json
A list of all K-Pop music groups, as taken from Wikipedia [here](https://en.wikipedia.org/wiki/Category:K-pop_music_groups).

## 📁 Raw Data
### all_ids.json
A file containing the ids of every post downloaded. Serves as a backup in case posts need to be re-requested from Reddit.

### all_posts.json

A dataset containing the key attributes (Score, Number of Comments, Upvote Ratio, etc.) of every post downloaded.

_(See test data/small_posts.json for a snippet of what this file looks like)_

### all_posts_complete.json
A more complete dataset that stores almost all attributes of every post downloaded.

_(See test data/small_posts_complete.json for a snippet of what this file looks like)_

## 📁 Scripts
### get_groups.py
Technologies Used: 
- mwclient (a library used to interface with Wikipedia's API)

Extracts a list of all K-Pop musical groups from the relevant Wikipedia page.

### get_posts.py
Technologies Used:
- PRAW (a Python wrapper for Reddit's API)
- Pushshift.io (a RESTful API built on top of Reddit's that provides enhanced functionality for searching Reddit submissions)
- PMAW (A multi-threaded warpper for Pushshift.io)

Downloads, aggregates, and organizes all submissions from r/kpop into a JSON file.

### process_posts.py

Takes the raw collection of all posts from the subreddit and organizes post metadata (number of upvotes, upvote ratio, etc.) by which K-Pop groups are named in the title. Also extracts important counts of certain attributes, such as how many total posts there are about a certain group and how many times each user has posted about a specific group.

### upload_posts.py
Technologies Used:
- pymongo (a python distribution containing tools for working with MongoDB)
- certifi (provides Mozilla's collection of Root Certificates)

Writes the processed dataset into MongoDB Cloud Atlas for API usage in the web app.

## 📁 Test Data

### small_posts.json
A small portion of all_posts.json used for testing purposes

### small_posts_complete.json
A small portion of all_posts_complete.json used for testing purposes.




