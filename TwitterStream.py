"""
Twitter Stream by Christopher Scott
http://www.scottdchris.com
"""
from twython import Twython
import django
import time
import pprint		#Pretty Print
import requests		#Requests


#Twython OAuth 1 Authentication
APP_KEY		= 'k7IKJEvxIYiro0I4M7yVg'
APP_SECRET	= #removed for git
OAUTH_TOKEN = '2213564010-I0jWjQQUTXmo8ySlPCcvP2lX3B42VQWWh6lVHGf'
OAUTH_TOKEN_SECRET = #removed for git

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