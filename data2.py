'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from wordcloud import WordCloud

# from wordcloud import wordcloud
#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!

ls=[[], []]
for each in tweetData:
    tweet = each["text"]
    tb= TextBlob(tweet)
    ls[0].append (tb.polarity)
    ls[1].append(tb.subjectivity)

print(tb.polarity)

num_bins = 3
n, bins, patches = plt.hist(ls[0], num_bins, facecolor = 'blue', alpha = 1)
plt.show()

def word_cloud_freq(tweetData):
    all_text = ""
    word_count = {}
    for each in tweetData:
        all_text += each["text"]
    all_text = all_text.lower()
    atb = TextBlob(all_text)
    word_list = atb.words
    for each in word_list:
        if len(each) > 3 and each.isalpha() == True and each != "https":
            if each not in word_count:
                word_count[each] = 1
            else:
                word_count[each] += 1
    wc = WordCloud(background_color="red", width=500,height=500,
    relative_scaling=1).generate_from_frequencies(list(word_count.items()))
    plt.imshow(wc, interpolation='bilinear')
    plt.show()
word_cloud_freq(tweetData)
