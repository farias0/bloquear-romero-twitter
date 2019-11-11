import tweepy

from twitter_credentials import CONSUMER_KEY, CONSUMER_SECRET

# TODO implement login database http://docs.tweepy.org/en/v3.5.0/auth_tutorial.html

def _oauth_login(): # TODO maybe run a webserver with callback for authentication??

  auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
  auth_url = auth.get_authorization_url()

  verify_code = input("Authenticate at %s and then enter you verification code here > " % auth_url) 
  auth.get_access_token(verify_code)

  return tweepy.API(auth)

class Mute:
  def __init__(self, ids):
    self.__api = _oauth_login()
    print("\nAuthenticated as @%s\n" % self.__api.me().screen_name)
    
    self.__ids = ids
    self.__was_muted = False

  @property
  def ids(self):
    return self.__ids

  @ids.setter
  def ids(self, ids):
    self.__ids = ids

  @property
  def was_muted(self):
    return self.__was_muted

  def mute(self): # TODO check conflicts if already muting or not
    for id in self.__ids:
      self.__api.create_mute(id)
    self.__was_muted = True     

  def unmute(self):
    for id in self.__ids:
      self.__api.destroy_mute(id)
    self.__was_muted = False

  @property
  def me(self):
    return "@" + self.__api.me().screen_name