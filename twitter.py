import dotenv
import os
from requests_oauthlib import OAuth1Session

dotenv.load_dotenv('.env')

consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')

print(consumer_key)
print(consumer_secret)
print(access_token)
print(access_token_secret)

session = OAuth1Session(consumer_key,
            client_secret=consumer_secret,
            resource_owner_key=access_token,
            resource_owner_secret=access_token_secret
        )

# The URL endpoint to update a status (i.e. Tweet)
url = 'https://api.twitter.com/1.1/statuses/update.json'

# The contents of status (i.e tweet text)
status = 'Only a fool tests the depth of a river with both feet. #afrobot'

# Send a POST request to the url with a 'status' parameter
def tweet(status):
    resp = session.post(url, {'status': status})
    return resp.text

# Show the text from the response 
print(resp.text)

