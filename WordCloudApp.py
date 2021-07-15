"""
Must install matplotlib and wordcloud with: 

    pip install matplotlib
    pip install wordcloud

"""

import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import sys, os
os.chdir(sys.path[0])

############ Reads Text ############

#text_file = 'obama_inaugural_address.txt'
text = open('obama_inaugural_address.txt' , mode='r' , encoding = 'utf-8').read()
stopwords = STOPWORDS

wc = WordCloud(
        background_color='white',
        stopwords= STOPWORDS,
        height = 600,
        width = 400
    )

wc.generate(text)

############ Stores To File ############

wc.to_file('WC_Output.png')