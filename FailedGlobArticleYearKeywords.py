import xml.etree.ElementTree as etree
import glob
import pandas as pd

for file in glob.glob('/Users/sydnimeyer/Downloads/metadata/journal-article-*.xml'):
    
    with open(file) as xmlfile:
        
        data = []

        tree = etree.parse(file)
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

#likely failure: eliminating articles with missing keywords
        if article_meta.findall('.//kwd-group') == None:
            print('0')
        
#setting keywords text
        for keyword in article_meta.findall('.//kwd-group/kwd'):
            keywords.append(keyword.text)

        data.append([
            article_year,
            keywords
            ])

# creating rows for data for Pandas DataFrame
rows.append({'Publication Year': article_year, 'Keywords': keywords})

out_df = pd.DataFrame(data, columns=['Publication year', 'Keywords'])

out_df.to_csv('glob_dates_keywords.csv', index=False)