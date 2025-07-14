from reddit_client import get_reddit_instance

def scrape_reddit_user(username):
    reddit = get_reddit_instance()
    user = reddit.redditor(username)

    posts = []
    comments = []

    for submission in user.submissions.new(limit=10):
        posts.append({
            "title": submission.title,
            "selftext": submission.selftext,
            "url": submission.url
        })

    for comment in user.comments.new(limit=20):
        comments.append({
            "body": comment.body,
            "link": f"https://www.reddit.com{comment.permalink}"
        })

    return posts, comments
