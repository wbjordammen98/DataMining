import keys
import tweepy as t
import json
from wordcloud import WordCloud

auth = t.OAuthHandler(keys.consumer_key, keys.secret_key)
auth.set_access_token(keys.access_token, keys.access_token_secret)

api = t.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

tweets = api.search(q="vote",count=3)

#print(tweets)

# Exercise: print screen name, user and text of the tweet.

#for tweet in tweets:
    #print(tweet.user.screen_name,":",tweet.text)

tweets = api.search(q="#collegefootball",count=2)

#for tweet in tweets:
    #print(tweet.user.screen_name,":",tweet.text)

# Places with trending tpoics.
trends_available = api.trends_available()

#print(len(trends_available))
#print(trends_available[:3])

world_trends = api.trends_place(id=1)

#print(world_trends)

outfile = open('world_trends.json','w')

json.dump(world_trends,outfile,indent=5)

trend_list = world_trends[0]['trends']

#print(trend_list)

# List comprehension to grab trends with more than 10,000 tweets.
trend_list = [ trend for trend in trend_list if trend['tweet_volume']]

from operator import itemgetter

trend_list.sort(key=itemgetter("tweet_volume"),reverse=True)

#print(trend_list[:5])

#for name in trend_list[:5]:
    #print(name['name'])

# Find the trending topics for NYC and create a wordcloud
nyc_trends = api.trends_place(id=2459115)

nyc_trend_list = nyc_trends[0]['trends']

#for name in nyc_trend_list[:5]:
    #print(name['name'])

#for vol in nyc_trend_list[:5]:
    #print(vol['volume'])

topics = {}

for trend in nyc_trend_list:
    topics[trend["name"]] = trend["tweet_volume"]

wordcloud = WordCloud(width=1600,height=900,prefer_horizontal=0.5,min_font_size=10,colormap="prism",background_color="white")

wordcloud = wordcloud.fit_words(topics)
wordcloud = wordcloud.to_file("Trending_NYC_Topics.png")
