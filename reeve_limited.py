#!/usr/bin/env python3
from pyvis.network import Network 
from IPython.core.display import display, HTML
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
graph = nx.Graph()
reeve_nouns = ['folk', 'business', 'Absolon', 'Nicholas', 'opinions', 'part', 'tale', 'man', 'Osewold', 'reeve', 'carpenters', 'craft', 'anger', 'heart', 'grouch', 'little', 'may', 'prosper', 'fruit', 'medlar', 'same', 'rubbish', 'straw', 'men', 'fear', 'fare', 'dance', 'world', 'pipe', 'sticks', 'nail', 'leek', 'power', 'desires', 'folly', 'anything', 'ashes', 'fire', 'coals', 'boasting', 'lying', 'greed', 'sparks', 'age', 'limbs', 'truth', 'years', 'tongue', 'chime', 'wretchedness', 'dotage', 'host', 'sermon', 'king', 'wit', 'day', 'holy', 'writ', 'devil', 'cobbler', 'shipman', 'physician', 'time', 'deptford', 'sires', 'displeased', 'fool', 'permissable', 'force', 'miller', 'terms', 'god', 'neck', 'piece', 'timber', 'trumpington', 'Cambridge', 'brook', 'bridge', 'mill', 'dwelling', 'peacock', 'bagpipe', 'fish', 'nets', 'game', 'belt', 'cutlass', 'blade', 'sword', 'dagger', 'pouch', 'peril', 'Sheffield', 'hose', 'face', 'nose', 'ape', 'skull', 'bully', 'person', 'hand', 'thief', 'grain', 'meal', 'sly', 'haughty', 'symkyn', 'wife', 'kin', 'parson', 'town', 'father', 'pan', 'brass', 'nunnery', 'holidays', 'tip', 'hood', 'gown', 'lady', 'water', 'ditch', 'disdain', 'cradle', 'boy', 'wench', 'eyes', 'glass', 'buttocks', 'breasts', 'hair', 'property', 'household', 'ancestry', 'churchs', 'goods', 'monopoly', 'milling', 'land', 'college', 'people', 'soler', 'hall', 'manciple', 'malady', 'fuss', 'scholars', 'mirth', 'amusement', 'buckler', 'sides', 'gear', 'guide', 'sack', 'head', 'hopper', 'trough', 'flour', 'bran', 'clerks', 'wolf', 'mare']
reeve_adj = ['foolish', 'clever', 'different', 'aggrieved', 'little', 'angry', 'old', 'dry', 'white', 'ripe', 'green', 'gone', 'continually', 'feeble', 'young', 'lordly', 'holy', 'waste', 'drunk', 'perilous', 'sharp', 'elegant', 'pug', 'bald', 'quarrelsome', 'brave', 'good-looking', 'thick', 'high', 'fair', 'headstrong', 'poor', 'eager', 'bold', 'implore', 'fast', 'done', 'ingenious', 'greatest', 'wisestfolk', 'wisest']
reeve_verbs = ['laughed', 'enjoyed', 'saw', 'criticized', 'prosper', 'repay', 'blearing', 'tricking', 'wanted', 'speak', 'play', 'done', 'reveals', 'fear', 'ripe', 'dance', 'pipe', 'sticks', 'have', 'gone', 'talk', 'making', 'began', 'amounts', 'made', 'preach', 'say', 'waste', 'deplored', 'begin', 'pray', 'answer', 'make', 'repel', 'force', 'told', 'tricked', 'scorn', 'leave', 'break', 'see', 'called', 'carried', 'played', 'mend', 'shoot', 'fostered', 'would', 'preserve', 'went', 'flirt', 'dared', 'cut', 'jealous', 'dangerous', 'think', 'besmirched', 'lie', 'determined', 'raised', 'ground', 'happened', 'lay', 'thought', 'die', 'stole', 'complained', 'fuss', 'blustered', 'swore', 'implore', 'give', 'pledge', 'steal', 'trickery', 'rob', 'needed', 'guide', 'lays', 'spoke', 'fares', 'welcome', 'knows', 'serve', 'expect', 'grind', 'carry', 'speed', 'stand', 'wags', 'falls', 'trick', 'take', 'wisest']
net = Network()
reeves_text = open("ReevesTale.txt")
cleaned_reeve = ''
for line in reeves_text:
    line = line.lower()
    if line != "\n":
        for word in line.split(' '):
            word = ''.join(x for x in word if x.isalpha())
            if word != '':
                cleaned_reeve = cleaned_reeve+ ' '+ word
reeve_list = cleaned_reeve.split(' ')
list_length = len(reeve_list)
#dictionary format:
#{noun: {noun: #, verb: #, adj: #...}
reeve_dict = {}
for index, word in enumerate(reeve_list):
    nearest_noun = ''
    nearest_adj = ''
    nearest_verb = ''
    if word in reeve_nouns:
        
        #find next noun
        noun_index = index+1

        for word in reeve_list[index + 1: list_length]:
            if word not in reeve_nouns:
                noun_index = noun_index + 1
            else:
                break
        if noun_index < list_length:
            nearest_noun = reeve_list[noun_index]
        if noun_index >= len(reeve_list):
                nearest_noun = ''
                noun_index = list_length
        #find either adjective is previous word or next closest adjective after but not exceeding a noun
        if index > 1:
            if reeve_list[index-1] in reeve_adj:
                nearest_adj = reeve_list[index-1]
                adj_index = index - 1
            else:
                for adj_index, word in enumerate(reeve_list[index + 1 : noun_index]):
                    if word in reeve_adj:
                        nearest_adj = word
                        break
        #find closest trailing verb not exceeding another noun
        verb_index = index + 1
        for verb_index, word in enumerate(reeve_list[index+1: noun_index]):
            if word in reeve_verbs:
                nearest_verb = word
                break
        main_noun = reeve_list[index]
        #print("Main Noun: " + main_noun)
        if reeve_list[index] not in reeve_dict:
            reeve_dict[main_noun] = {}
        #print("Nearest Noun: " + nearest_noun)
        if nearest_noun != '':
            if nearest_noun not in reeve_dict[main_noun]:
                reeve_dict[main_noun][nearest_noun] = 1
            else:
                reeve_dict[main_noun][nearest_noun] = reeve_dict[main_noun][nearest_noun] + 1
        #print("Nearest Adjective: " + nearest_adj)
        if nearest_adj != '':
            if nearest_adj not in reeve_dict[main_noun]:
                reeve_dict[main_noun][nearest_adj] = 1
            else:
                reeve_dict[main_noun][nearest_adj] = reeve_dict[main_noun][nearest_adj] + 1
        #print("Nearest Verb: " + nearest_verb)
        if nearest_verb != '':
            if nearest_verb not in reeve_dict[main_noun]:
                reeve_dict[main_noun][nearest_verb] = 1
            else:
                reeve_dict[main_noun][nearest_verb] = reeve_dict[main_noun][nearest_verb] + 1

for main_noun in reeve_dict:
    print(main_noun)
    print(reeve_dict[main_noun])
#{noun: {noun: #, verb: #, adj: #...}

for word in reeve_adj:
    graph.add_node(word)
for word in reeve_verbs:
    graph.add_node(word)
for word in reeve_nouns:
    graph.add_node(word)

for main_noun in reeve_dict:
    for connection in reeve_dict[main_noun]:
        graph.add_edge(main_noun, connection)
pos = nx.circular_layout(graph)
nx.draw(graph, pos=pos, with_labels=True)
plt.savefig("reeve_circ.png") # save as png
plt.show() # display