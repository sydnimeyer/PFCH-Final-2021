import xml.etree.ElementTree as etree
import glob
import pandas as pd

keywords = []

#creating structure for Pandas dataframe
df_cols = ['Keywords']
rows = []

for file in glob.glob('/Users/sydnimeyer/Downloads/metadata/kwd/*.xml'):
    
    with open(file) as xmlfile:

        tree = etree.parse(file)
        root = tree.getroot()

# #defining tree structure
        article_meta = tree.find('front').find('article-meta')

# #setting keywords text
        for keyword in article_meta.findall('.//kwd-group/kwd'):
            keywords.append(keyword.text)

# # creating rows for data for Pandas DataFrame
rows.append({'Keywords': keywords})

out_df = pd.DataFrame(rows, columns=df_cols)

out_df.to_csv('kwdglob_keywords.csv', index=False)