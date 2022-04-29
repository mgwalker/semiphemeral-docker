import json
import sys
import tweepy

# You can find the status ID to delete by looking at the network panel in the
# browser dev tools when you navigate to your own "tweets and replies" page.
# Look for the XHR to UserTweetsAndReplies. You're looking for the id_str field
# on your tweet. If yours is a retweet, keep in mind that your retweet has a
# separate ID from the original tweet, but both of them show up in the XHR
# response, so you'll have to dig through it to find the right one.

if len(sys.argv) < 2:
    print("Need to specify a status ID")
    quit()

config = json.loads(open("config/settings.json").read())

auth = tweepy.OAuthHandler(config["api_key"], config["api_secret"])
auth.set_access_token(config["access_token_key"], config["access_token_secret"])

api = tweepy.API(auth)
print("deleting tweet with status", sys.argv[1])
api.destroy_status(sys.argv[1])
