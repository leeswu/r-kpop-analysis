from attr import Attribute
from pmaw import PushshiftAPI
import prawcore
import praw
import datetime
import json
import time
import config as cfg

api = PushshiftAPI()

CLIENT_ID = cfg.PRAW_ID
SECRET_KEY = cfg.PRAW_SECRET

reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=SECRET_KEY, user_agent="MyAPI")
data = {}


DATE_CREATED = 1246818874
START_DATE = "6/30/2022"
END_DATE = "07/01/2022"

start_date = int(datetime.datetime.strptime(
    START_DATE, "%m/%d/%Y").replace(tzinfo=datetime.timezone.utc).timestamp())
end_date = int(datetime.datetime.strptime(
    END_DATE, "%m/%d/%Y").replace(tzinfo=datetime.timezone.utc).timestamp())

# Get ID info for all posts using PMAW
posts = api.search_submissions(
    after=DATE_CREATED,
    before=end_date,
    filter=['id'],
    subreddit="kpop",
    limit=None,
    metadata=True,
)

ids = [post['id'] for post in posts]
post_names = [f"t3_{id}" for id in ids]

with open('all_ids.json', 'w') as f:
    json.dump(post_names, f, indent=2)

gen = reddit.info(fullnames=post_names)

start_time = time.time()

for i, post in enumerate(gen):  # All relevant submission IDs requested from PMAW
    print(f"Processing post:{i + 1}")
    try:
        if post.selftext != ('[deleted]' or '[removed]'):  # Filter removed posts
            data[post.title] = {
                "Author": None,
                "Author Flair": None,
                "Time Created": post.created_utc,
                "Distinguished": post.distinguished,
                "Edited": post.edited,
                "id": post.id,
                "Is Original": post.is_original_content,
                "Is Self": post.is_self,
                "Link": post.shortlink,
                "Link Flair Text": None,
                "Locked": post.locked,
                "Name": post.name,
                "NSFW": post.over_18,
                "Num Comments": post.num_comments,
                "Permalink": post.permalink,
                "Score": post.score,
                "Selftext": post.selftext,
                "Spoiler": post.spoiler,
                "Stickied": post.stickied,
                "Upvote Ratio": post.upvote_ratio,
                "URL": post.url
            }
            if post.author:  # Add Author info, if available
                data[post.title]["Author"] = f"u/{post.author.name}"
                # if hasattr(post, "author_flair_text") and post.author_flair_text:
                #     data[post.title]["Author Flair"] = post.author_flair_text
            try:
                data[post.title]["Link Flair Text"] = post.link_flair_text
                # data[post.title]["Link Flair id"] = post.link_flair_template_id
                data[post.title]["Author Flair"] = post.author_flair_text
            except AttributeError as e:
                print(e)
                pass
    except prawcore.exceptions.NotFound as e:  # Error handling
        print(e)
        with open('all_posts_complete.json', 'w') as f:
            json.dump(data, f, indent=2)
        continue
    except Exception as e:
        print(e)
        with open('all_posts_complete.json', 'w') as f:
            json.dump(data, f, indent=2)
        continue
print(len(data))

with open('all_posts_complete.json', 'w') as f:
    json.dump(data, f, indent=2)

print("%s seconds" % (time.time() - start_time))

