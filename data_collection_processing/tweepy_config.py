import tweepy
COLS = ['id', 'created_at', 'original_text','clean_text', 'retweet_count', 'hashtags','mentions', 'original_author']
politicians = ['SenSanders','realDonaldTrump', 'JoeBiden', 'andrewcuomo', 'TeamPelosi', 'NikkiHaley', 'MittRomney', 'Mike_Pence','SenatorCollins','PeteButtigieg']
RETWEET_COLS = ['original_tweet_id','retweet_id','type','created_at','source','favorite_count','retweet_count','original_author']

CONSUMER_KEY    = "ZrMYVz4BAb4YdafAIceEVF7iU"
CONSUMER_SECRET = "Wxs0USX2wcqMd1cOorNLn58U4wS9mocLmHqRuETd97giJ4H4CX"
ACCESS_KEY      = "1284460786610368513-jL7KyWzoDAPR07BCIiEjKQoR2B29TY"
ACCESS_SECRET   = "fdtTCHTXDMxzGmIx7xg2Xlz8k9e3OdYTuXGhKNm5zIueG"
print("--- Authorize Twitter; Initialize Tweepy ---")
auth 		= tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api 		= tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)