import snscrape.modules.twitter as sntwitter
import datetime

def scan_tweets(keyword, limit=10):
    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'{keyword} since:{(datetime.date.today() - datetime.timedelta(days=1))}').get_items()):
        if i >= limit:
            break
        tweets.append({
            "content": tweet.content,
            "username": tweet.user.username,
            "date": tweet.date.strftime('%Y-%m-%d %H:%M:%S'),
        })
    return tweets
