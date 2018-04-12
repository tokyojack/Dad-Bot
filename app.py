import requests
from apscheduler.schedulers.blocking import BlockingScheduler
from twitter import TwitterError, Api

twitter_api = Api(consumer_key='',
          consumer_secret='',
          access_token_key='',
          access_token_secret='')

def get_joke():
    return requests.get(
        "https://icanhazdadjoke.com",
        headers={"Accept": "application/json"}
    ).json()['joke']

def tweet_message():
    try:
        credentials = twitterAPI.VerifyCredentials()
        print("--------- Stats ---------")
        print(f"Follower Count: {credentials.followers_count}")
        print(f"Friends Count: {credentials.friends_count}")
        
        joke = get_joke()
        twitter_api.PostUpdate(joke)
        print(f"Tweeted out: {joke}")

    except TwitterError as exception:
        print(f"EXCEPTION: {exception}")


if __name__ == "__main__":
    print("Application started")
    scheduler = BlockingScheduler()
    scheduler.add_job(tweet_message, 'interval', hours=1)
    scheduler.start()
