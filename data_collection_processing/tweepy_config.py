import tweepy
COLS = ['id', 'created_at', 'original_text','clean_text', 'retweet_count', 'hashtags','mentions', 'original_author']
politicians = ['SenSanders','realDonaldTrump', 'JoeBiden', 'andrewcuomo', 'TeamPelosi', 'NikkiHaley', 'MittRomney', 'Mike_Pence','SenatorCollins','PeteButtigieg']
RETWEET_COLS = ['original_tweet_id','retweet_id','type','created_at','source','favorite_count','retweet_count','original_author']
from login_credentials import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

print("--- Authorize Twitter; Initialize Tweepy ---")
auth 		= tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api 		= tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)