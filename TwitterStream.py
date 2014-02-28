"""
Twitter Stream by Christopher Scott
http://www.scottdchris.com
"""
from twython import Twython
import django
import time
import pprint		#Pretty Print
import requests		#Requests
import TwitterStreamKeys

#Twython OAuth 1 Authentication
APP_KEY				= TwitterStreamKeys.keys['APP_KEY']
APP_SECRET			= TwitterStreamKeys.keys['APP_SECRET']
OAUTH_TOKEN 		= TwitterStreamKeys.keys['OAUTH_TOKEN']
OAUTH_TOKEN_SECRET 	= TwitterStreamKeys.keys['OAUTH_TOKEN_SECRET']

listOfTweets = ''

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
results = twitter.search(q='WTPUMass', result_type='recent', count = '50')

for tweet in results['statuses']:
	#pprint.pprint(tweet['entities']['media'])
	imageURL = ''
	user_handle = ('@' + tweet['user']['screen_name']).encode('ascii','ignore')
	tweetText = tweet['text'].encode('ascii','ignore')
	
	if 'media' in tweet['entities']:
		imageURL = tweet['entities']['media'][0]['media_url']
		
	listOfTweets += "%s, %s, %s\n" % (user_handle, tweetText, imageURL)

#print listOfTweets
csvFile = open('Tweets.csv', 'wb')
csvFile.write(listOfTweets)
csvFile.close()

time.sleep(1) #Script runs once every 1:01 mins to avoid Twitter API Rate Limit Error of 15 calls per 15 minutes