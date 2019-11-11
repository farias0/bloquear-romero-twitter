import tweepy

from twitter_credentials import CONSUMER_KEY, CONSUMER_SECRET

def _oauth_login():

  auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
  auth_url = auth.get_authorization_url()

  verify_code = input("Authenticate at %s and then enter you verification code here > " % auth_url) 
  auth.get_access_token(verify_code)

  return tweepy.API(auth)

class Block:
  def __init__(self, id_to_block):
    self.__api = _oauth_login()
    print("\nAuthenticated as: %s\n" % self.__api.me().screen_name)
    
    self.__id_to_block = id_to_block

  def get_id_to_block(self):
    return self.__id_to_block

  def block(self): # TODO

  def unblock(self): # TODO