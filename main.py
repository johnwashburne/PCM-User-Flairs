import praw
import pickle

reddit = praw.Reddit(client_id='idhere', client_secret='secrethere',
                     password='password', username='username',
                     user_agent='agent')

subreddit = reddit.subreddit('PoliticalCompassMemes')
top_posts = list(subreddit.top('all', limit=1000))

authors = pickle.load(open('authors.p', 'rb'))

flairs = pickle.load(open('flairs.p', 'rb'))
count = 0
for submission in top_posts:

    try:
        print(submission.title, submission.ups, 'num left:', count)
    except:
        print('emoji encountered')

    
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        if comment.author not in authors:
            if comment.author_flair_text != None:
                authors[comment.author] = comment.author_flair_text
                print(comment.author_flair_text)
                flairs.append(comment.author_flair_text)

    count += 1

pickle.dump(flairs, open('flairs.p','wb'))
pickle.dump(authors, open('authors.p', 'wb'))
