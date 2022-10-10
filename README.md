# collect_realtime_tweets
Collect realtime tweets given a set of keywords. Please note that tweets are collected at a limited rate.

## Prerequisites
- Python 3
- [Tweepy](https://www.tweepy.org/)

## Keywords
The files `words_about_crime.txt` and `words_about_health.txt` store lists of words that are closely related to the topic `crime` and `health`. They are manually defined.


### 1. Create folders to save data ###
Create folders at the project root, e.g., ``crime``, ``health``. Suppose we want to collect tweets involving the topics crime and health.

### 2. Run Python code to collect data ###
```python
python get_crime.py

python get_health.py
``` 

*data in `crime/` and `health/` are in JSON format*
```python
columns (text or extended_tweet['full_text'])
	Index(['created_at', 'id', 'id_str', 'text', 'source', 'truncated',
       'in_reply_to_status_id', 'in_reply_to_status_id_str',
       'in_reply_to_user_id', 'in_reply_to_user_id_str',
       'in_reply_to_screen_name', 'user', 'geo', 'coordinates', 'place',
       'contributors', 'retweeted_status', 'is_quote_status', 'quote_count',
       'reply_count', 'retweet_count', 'favorite_count', 'entities',
       'favorited', 'retweeted', 'filter_level', 'lang', 'timestamp_ms',
       'possibly_sensitive', 'extended_entities', 'display_text_range',
       'extended_tweet', 'quoted_status_id', 'quoted_status_id_str',
       'quoted_status', 'quoted_status_permalink', 'withheld_in_countries',
       'limit'],
      dtype='object')
```
      
### 3. Customization ###
Create your own `words_about_XXX.txt` and `get_XXX.py`.
