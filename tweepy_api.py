import tweepy
auth = tweepy.OAuthHandler("1284460786610368513-kQgCNaa42tjuRqB6pHnP2nLG7G0zPc","nvlSUik8RK33xoVC3cxCJyz6i3r9Z8zGZ6JaVGzN588GI")
auth.set_access_token("ZrMYVz4BAb4YdafAIceEVF7iU", "Wxs0USX2wcqMd1cOorNLn58U4wS9mocLmHqRuETd97giJ4H4CX")
# auth.set_access_token("1284460786610368513-kQgCNaa42tjuRqB6pHnP2nLG7G0zPc", "nvlSUik8RK33xoVC3cxCJyz6i3r9Z8zGZ6JaVGzN588GI")

try:
    api.verify_credentials()
    print("Authentication OK")
except Error as E:
    print(f"Error{E} during authentication")