#!/usr/bin/env python3
from wordcloud import WordCloud
import matplotlib.pyplot as plt
#import data:
reeves_tale = open('ReevesTale.txt').read()
millers_tale = open('millersTale.txt').read()
wife_tale = open('wifeOfBath.txt').read()

#generate a word cloud based on the reeves tale:
wordcloud_reeve = WordCloud(font_path = '/Library/Fonts/Arial Unicode.ttf', background_color="white", width=3000, height=2000, max_words=500).generate(reeves_tale)

plt.figure(figsize=[15,10])
plt.imshow(wordcloud_reeve, interpolation="bilinear")
plt.axis("off")
plt.savefig("reeveImage.png")
print("done with wordcloud")