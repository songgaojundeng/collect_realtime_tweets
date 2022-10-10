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

### 3. Customization ###
Create your own `words_about_XXX.txt` and `get_XXX.py`.
