# -*- coding: utf-8 -*-

# import libraries 

import os
from PIL import Image

import nltk
import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.ndimage import gaussian_gradient_magnitude
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS

# import mask image. Search for stencil image for better results

mask = np.array(Image.open("darthvader01.png"))

# define function for grayscale coloring

def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

# Load and text and decode 
text = open(('oe2022_text.txt'), "rb").read().decode('UTF-8', errors='replace')

# Load stopwords for PT languguage from nlkt 
stopwords = nltk.corpus.stopwords.words('portuguese')

# Create a list with specific words for the OE2022 document
newStopWords = ['n','artigo','Lei','Proposta','redação','atual','disposto','prevista','o','Decreto','termo','âmbito',
				'número','serviço','Código', 'anterior', 'O'
				]
# Extend stopword with our own stopwords
stopwords.extend(newStopWords)

# Create Worldcloud

wc = WordCloud(max_words=5000, width=1600, height=800, stopwords=stopwords, mask=mask).generate(text)

# Recolor our Wordcloud

plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3),
           interpolation="bilinear")

# Save worldcloud file

wc.to_file("OE2022_WC.png")



