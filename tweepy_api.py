import tweepy
auth = tweepy.OAuthHandler(consumer_key="ZrMYVz4BAb4YdafAIceEVF7iU", consumer_secret="Wxs0USX2wcqMd1cOorNLn58U4wS9mocLmHqRuETd97giJ4H4CX")
auth.set_access_token(key="1284460786610368513-VFyAcPWdI4uJplrQsuZdh5327trugE", secret="972ueh2EHKtPYoAW0PVrfbNuVmjI5t0YP7R8ZKQJkBplg")

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")