import tweepy
from MiningListener import MineListener
import time

#TODO: Read from the file instead of hardcoding?
def getAuthenticatedAPI():
	auth = tweepy.OAuthHandler('WuOEiRzGJzlHt1H2imTCPUpfR','X47THIKVxHqGxdHv8AkrcwyU3bH1NW91gIBang8mamhGim7n2Z')
	auth.set_access_token('778344887867416576-jKrxd6xzfdCispj9HTPpN4DEZwkkIJV', 'vgLsPQLtoRaIqfJjaRd7jLUvVMyhazYsrYhvLucjv9Q5r')
	api = tweepy.API(auth)
	return api



api = getAuthenticatedAPI()
listener = MineListener()

#Create stream object
stream = tweepy.Stream(auth = api.auth, listener = listener)

#Get stream running //  Put keywords here
stream.filter(track = ["party","game","sports","feelings"])

#For testing purposes; limits count of tweets to 10
while (len(MineListener.tweets) < 5):
	time.sleep(5)

#Prints out all gathered twitter data
for tweet in MineListener.tweets:
	tweet.printData()
	print ''