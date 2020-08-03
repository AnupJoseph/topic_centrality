import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("ZrMYVz4BAb4YdafAIceEVF7iU", "Wxs0USX2wcqMd1cOorNLn58U4wS9mocLmHqRuETd97giJ4H4CX")
auth.set_access_token("1284460786610368513-kQgCNaa42tjuRqB6pHnP2nLG7G0zPc","nvlSUik8RK33xoVC3cxCJyz6i3r9Z8zGZ6JaVGzN588GI")
api = tweepy.API(auth)
# test authentication
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")