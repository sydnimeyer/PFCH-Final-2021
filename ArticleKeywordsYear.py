import xml.etree.ElementTree as etree
import pandas as pd

data = []

tree = etree.parse('/Users/sydnimeyer/Downloads/metadata/journal-article-10.13169_worlrevipoliecon.8.4.0542.xml')
root = tree.getroot()
keywords = []

#creating structure for Pandas dataframe
df_cols = ['publication year', 'keywords']
rows = []

#defining tree structure
article_meta = tree.find('front').find('article-meta')

#setting article year attribute
if article_meta.find('pub-date') != None:
    article_year = int(article_meta.find('pub-date').find('year').text)


for keyword in article_meta.findall('.//kwd-group/kwd'):
    keywords.append(keyword.text)   

data.append([
    article_year,
    keywords
])

# creating rows for data for Pandas DataFrame
rows.append({'Publication Year': article_year, 'Keywords': keywords})

out_df = pd.DataFrame(data, columns=['Publication year', 'Keywords'])

out_df.to_csv('article_dates_keywords.csv', index=False)