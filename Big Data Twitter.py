# Code by Michael Odbert and Mahnaz Roshanaei
# Big Data HCI
#
# Twitter data gathering software
#
# HOW IT WORKS:
# The code creates a file with the date as the file name (only run once a day max)
# The twitter database is accessed so it's API can be used
# The user Enters the last file they entered, the last tweet_id is used from that
# The code grabs the most recent tweets all the way to the last tweet grabbed
# this is done so that the code only hast be be run once every few days
# The new tweet data is put into the new file and saved
#
#
#
################# DON'T RUN THE CODE MORE THAN ONCE A DAY!!!!! #################
#
#
#
#Python wrapper for Twitter
import tweepy

import time
import datetime

# Create the file that will hold all tweets collected
# Creates a .txt file with the DAY as the title
file1 = str(datetime.datetime.now())
file1 = file1[:10]
file1 = file1 +'.txt'
tweet_file = open(file1,'w')


# Michael Odbert's Developer Tokens
consumer_token = ''
consumer_secret = ''
access_token = ''
access_secret = ''

# Authentication code for access to twitter stream
auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(access_token, access_secret)
# Setting the twitter api 
api = tweepy.API(auth)




# Search Parameters
search_term = '#dressfriday'            #Return tweets containing the search term
max_count = 100                   #How many tweets to return (max 100)
language = 'en'                 #What language returned tweets are in (en=english)


#opens the last file
lastfile = raw_input("Enter the last file created: ")
with open(lastfile+'.txt', 'r') as f:
  last_tweet_ID = f.readline()
  
sinceID = last_tweet_ID         #384414271133982720
maxID = 999999999999999999      #Largest number that max_id can be




# Each search call can only return 100 results
# The search call can be called many times
for x in range(0,30):
    result = api.search(q=search_term,
                        lang=language,
                        count= max_count,
                        since_id=sinceID,
                        max_id=maxID)
    for tweet in result:
        # Sets maxID to the lowest tweet ID in returned set
        # Used for the next iteration to work backwards in the list of tweets
        if tweet.id < maxID:
            maxID = tweet.id
        # Write tweet informtion to a .txt file
        tweet_file.write(str(tweet.id))
        tweet_file.write('\n')
        tweet_file.write(str(tweet.created_at))
        tweet_file.write('\n')
        tweet_file.write(str(tweet.user.name.encode('utf-8')))
        tweet_file.write('\n')
        tweet_file.write(tweet.text.encode('utf-8'))
        tweet_file.write('\n')
        tweet_file.write('\n')
        

    # Decrease maxID so there are no duplicate tweets
    maxID = maxID-1


tweet_file.close()
