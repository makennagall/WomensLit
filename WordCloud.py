#!/usr/bin/env python3
from wordcloud import WordCloud
import matplotlib.pyplot as plt
#import data:
reeves_tale = open('ReevesTale.txt')
#Noun, adjectives and verbs list:
reeve_important = ['folk', 'business', 'absolon', 'nicholas', 'opinions', 'part', 'tale', 'man', 'Osewold', 'reeve', 'carpenters', 'craft', 'anger', 'heart', 'grouch', 'little', 'may', 'prosper', 'fruit', 'medlar', 'same', 'rubbish', 'straw', 'men', 'fear', 'fare', 'dance', 'world', 'pipe', 'sticks', 'nail', 'leek', 'power', 'desires', 'folly', 'anything', 'ashes', 'fire', 'coals', 'boasting', 'lying', 'greed', 'sparks', 'age', 'limbs', 'truth', 'years', 'tongue', 'chime', 'wretchedness', 'dotage', 'host', 'sermon', 'king', 'wit', 'day', 'holy', 'writ', 'devil', 'cobbler', 'shipman', 'physician', 'time', 'deptford', 'sires', 'displeased', 'fool', 'permissable', 'force', 'miller', 'terms', 'god', 'neck', 'piece', 'timber', 'trumpington', 'Cambridge', 'brook', 'bridge', 'mill', 'dwelling', 'peacock', 'bagpipe', 'fish', 'nets', 'game', 'belt', 'cutlass', 'blade', 'sword', 'dagger', 'pouch', 'peril', 'Sheffield', 'hose', 'face', 'nose', 'ape', 'skull', 'bully', 'person', 'hand', 'thief', 'grain', 'meal', 'sly', 'haughty', 'symkyn', 'wife', 'kin', 'parson', 'town', 'father', 'pan', 'brass', 'nunnery', 'holidays', 'tip', 'hood', 'gown', 'lady', 'water', 'ditch', 'disdain', 'cradle', 'boy', 'wench', 'eyes', 'glass', 'buttocks', 'breasts', 'hair', 'property', 'household', 'ancestry', 'churchs', 'goods', 'monopoly', 'milling', 'land', 'college', 'people', 'soler', 'hall', 'manciple', 'malady', 'fuss', 'scholars', 'mirth', 'amusement', 'buckler', 'sides', 'gear', 'guide', 'sack', 'head', 'hopper', 'trough', 'flour', 'bran', 'clerks', 'wolf', 'mare', 'foolish', 'clever', 'different', 'aggrieved', 'little', 'angry', 'old', 'dry', 'white', 'ripe', 'green', 'gone', 'continually', 'feeble', 'young', 'lordly', 'holy', 'waste', 'drunk', 'perilous', 'sharp', 'elegant', 'pug', 'bald', 'quarrelsome', 'brave', 'good-looking', 'thick', 'high', 'fair', 'headstrong', 'poor', 'eager', 'bold', 'implore', 'fast', 'done', 'ingenious', 'greatest', 'wisestfolk', 'wisest', 'laughed', 'enjoyed', 'saw', 'criticized', 'prosper', 'repay', 'blearing', 'tricking', 'wanted', 'speak', 'play', 'done', 'reveals', 'fear', 'ripe', 'dance', 'pipe', 'sticks', 'have', 'gone', 'talk', 'making', 'began', 'amounts', 'made', 'preach', 'say', 'waste', 'deplored', 'begin', 'pray', 'answer', 'make', 'repel', 'force', 'told', 'tricked', 'scorn', 'leave', 'break', 'see', 'called', 'carried', 'played', 'mend', 'shoot', 'fostered', 'would', 'preserve', 'went', 'flirt', 'dared', 'cut', 'jealous', 'dangerous', 'think', 'besmirched', 'lie', 'determined', 'raised', 'ground', 'happened', 'lay', 'thought', 'die', 'stole', 'complained', 'fuss', 'blustered', 'swore', 'implore', 'give', 'pledge', 'steal', 'trickery', 'rob', 'needed', 'guide', 'lays', 'spoke', 'fares', 'welcome', 'knows', 'serve', 'expect', 'grind', 'carry', 'speed', 'stand', 'wags', 'falls', 'trick', 'take', 'wisest']
cleaned_reeve = ''
for line in reeves_tale:
    line = line.lower()
    if line != "\n":
        for word in line.split(' '):
            word = ''.join(x for x in word if x.isalpha())
            if word != '':
                cleaned_reeve = cleaned_reeve+ ' ' + word
print(cleaned_reeve)
refined_list = ''
for word in cleaned_reeve.split(' '):
    #print(word)
    if word in reeve_important:
        refined_list = refined_list + ' ' + word
#print(refined_list)
#generate a word cloud based on the reeves tale:
wordcloud_reeve = WordCloud(font_path = '/Library/Fonts/Arial Unicode.ttf', background_color="white", width=3000, height=2000, max_words=500).generate(refined_list)

plt.figure(figsize=[15,10])
plt.imshow(wordcloud_reeve, interpolation="bilinear")
plt.axis("off")
plt.savefig("reeveWordCloud.png")
