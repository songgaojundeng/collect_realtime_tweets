import tweepy
import json
import sys,os
import time,datetime
# from threading import Thread
from tweepy.streaming import StreamListener
from tweepy import Stream
# from urllib3.exceptions import ProtocolError

consumer_key = 'cgJjHjXiZuIcKvrTg22PPdZdE'
consumer_secret = '3voh2dvLpZDZsG9ov6FOEHS3baS9g4syorraE1IhhYFiL8w55j'
access_token = '3810742695-IK89MzHkUGnDGzLPrgBmDVFlHUODbfLzPwIOJNs'
access_token_secret = '8znCM24sT1GK3aMwUEXxiR65Ze4x8a6VvwCyb18SthHyh'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def get_proper_file(key_type):
    cur_time = time.strftime('%Y-%m-%d', time.localtime())
    return open(key_type+'/'+cur_time+'.json','a')

def get_file_size(key_type): # mb gb ->30
    cur_time = time.strftime('%Y-%m-%d', time.localtime())
    file_name = (key_type + '/'+cur_time+'.json')
    size = os.path.getsize(file_name)/float(1<<20)
    return size

class StdOutListener(StreamListener):

    def __init__(self,key_type):
        self.key_type = key_type
        self.save_file = get_proper_file(key_type)
        

    def on_data(self, data):
        now = datetime.datetime.now()
        today8am = now.replace(hour=8, minute=0, second=0) #8
        today24pm = now.replace(hour=21, minute=59, second=0) #23
        size = get_file_size(self.key_type)
        if size > 3648: #2648
            print(self.key_type,"File size exceed",size,'MB')
            self.save_file.close()
            time.sleep(7200) #3600
            
            return False


        if now > today8am and now < today24pm:
            json_data = json.loads(data)
            if "delete" not in json_data: #  first level keys
                print(self.key_type,data[18:71])
                self.save_file.write(data)
                
            return True
        
        print("Evening time")
        time.sleep(7200)  
        return False
        

    def on_error(self, status):
        # If the error code is 401, which is the error for bad credentials
        print('Encountered error with status code:', status)

        return False

    # When a deleted tweet appears
    def on_delete(self):        
        print("Delete notice")
        return

    # When reach the rate limit
    def on_limit(self, track):        
        print("Rate limited, continuing")        
        return True
    
    def on_timeout(self):
        print(sys.stderr, 'Timeout...')        
        return 
    def om_exception(self, exception):
        print(exception)
        return

def get_tweets(key_type, words):
    print(key_type,' start fetching')
    stream = Stream(auth, StdOutListener(key_type))
    stream.filter(languages=['en'], track=words, stall_warnings=True)
    time.sleep(10)

if __name__ == '__main__':
    health_file = open('words_about_health.txt')
    health_words = health_file.read().split("\n")
    health_file.close()

    while True:
        try:
            get_tweets('health', health_words)
        except Exception as e:
            print(e.__doc__)
        continue