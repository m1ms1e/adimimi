import tweepy



# Consumer keys and access tokens, used for OAuth
consumer_key = 'l8D0T6R8EBLYFtno00UQC7YUf'
consumer_secret = 'IJ3Vrjud16hjbAKvtWxE6QlcyWeluo7vUFliRVHFAwqiiqg99v'
access_token = '567605134-eoUluFNsxu0X4ZiXfcrcS41kQdSewtWAcU5PnsPz'
access_token_secret = 'GOS1Bd0zPvYFO0Pih4I5nLoUzXRgvqEfvGpZ3HmSayChQ'
 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)
 
# Sample method, used to update a status
api.update_status('Hello Python Central!')





#def tweeter():


 # user = "@adismooth"

  #twitter_search_endpoint = "https://api.twitter.com/1.1/search/tweets.json"
  #payload = {"q": user, "appid": "50586a3fda23cc18fb9d9fadb72b9d7b"}

  #tweeter_response = requests.get(twitter_search_endpoint, params=payload)
  #tweeter_data = tweeter_response.json()
  
  #temperature = weather_data['main']['temp']