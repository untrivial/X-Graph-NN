import os
import tweepy

class XAPI:
    def __init__(self, api_key=None, api_secret_key=None):
        self.bearer_token = os.environ.get('X_BEARER_TOKEN')
        self.api_key = api_key or os.environ.get('X_API_KEY')
        self.api_secret_key = api_secret_key or os.environ.get('X_API_SECRET_KEY')

        if self.bearer_token:
            self.client = tweepy.Client(bearer_token=self.bearer_token)
            self.auth = tweepy.OAuth2BearerHandler(self.bearer_token)
        elif self.api_key and self.api_secret_key:
            self.client = tweepy.Client(consumer_key=self.api_key, consumer_secret=self.api_secret_key)
            self.auth = tweepy.OAuthHandler(self.api_key, self.api_secret_key)
        else:
            raise ValueError("Either X_BEARER_TOKEN or both X_API_KEY and X_API_SECRET_KEY must be set")

        self.api = tweepy.API(self.auth)

    def get_user_id(self, handle):
        response = self.client.get_user(username=handle)
        return response.data.id
    
    def get_user_following(self, user_id):
        return self.client.get_users_following(id=user_id)

if __name__ == '__main__':
    x_api = XAPI()
    print(x_api.get_user_id('chentropic'))
