import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import re

import matplotlib.pyplot as plt
import wordcloud

#This word cloud was crafted by following the "Generating WordClouds in Python" tutorial from Duong Vu, found here: https://www.datacamp.com/community/tutorials/wordcloud-python

#load DataFrame
df = pd.read_csv('/Users/sydnimeyer/Downloads/kwdglob_keywords.csv', index_col=0)

#tests:
#print('dataframe shape is', df.shape)
#df.head()

#clean data
pattern = re.compile(r'^\w[0-9]{2}')
filter = df[df['Keywords'].str.contains(pattern)==True]
df = df[~filter]

#create WordCloud
text = df.Keywords

wc = WordCloud(max_font_size=60, max_words=200, background_color="black").generate(text)

plt.figure()
plt.imshow(wc,interpolation='bilinear')
plt.axis("off")
plt.show()

wc.to_file('img/AKochMoneyWordCloud.png')