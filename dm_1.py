import keys
import tweepy as t

auth = t.OAuthHandler(keys.consumer_key, keys.secret_key)
auth.set_access_token(keys.access_token, keys.access_token_secret)

api = t.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.get_user("JPetrucci")

print(user.name)
print(user.description)
print(user.status.text)
print(user.followers_count)
print(user.geo_enabled)

me = api.me
#print(me.name)

followers = []

#print(user)

cursor = t.Cursor(api.followers, screen_name="JPetrucci")

for account in cursor.items(10):
    followers.append(account.screen_name)

#print(followers)

friends = []

cursor = t.Cursor(api.friends, screen_name="JPetrucci")

for friend in cursor.items(10):
    friends.append(friend.screen_name)

#print(friends)

jp_tweets = api.user_timeline(screen_name="JPetrucci", count=5)

#for tweet in jp_tweets:
    #print(f'{tweet.user.screen_name}: {tweet.text}\n')

mytweets = api.home_timeline()

for tweets in mytweets:
    print(f'{tweet.text}\n')