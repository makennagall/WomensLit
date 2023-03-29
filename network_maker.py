#!/usr/bin/env python3
from pyvis.network import Network 
from IPython.core.display import display, HTML


import pandas as pd

net = Network()
#create library of word connections:
reeves_text = open("ReevesTale.txt")
cleanedReeve = ''
for line in reeves_text:
    line = line.lower()
    if line != "\n":
        for word in line.split(' '):
            word = ''.join(x for x in word if x.isalpha())
            if word != '':
                cleanedReeve = cleanedReeve + ' '+ word
print(cleanedReeve)
wordDict = {}
clean_r_list = cleanedReeve.split(' ')
for index, word in enumerate(clean_r_list):
    if index < len(clean_r_list)-1:
        if word in wordDict:
            wordDict[word].append(clean_r_list[index + 1])
        else:
            wordDict[word] = [clean_r_list[index + 1]]
print(wordDict)
for key in wordDict:
    count = len(wordDict[key])
    net.add_node(key, label = key)
for key in wordDict:
    for word in wordDict[key]:
        net.add_edge(key, word) 
net.show('networkVisual.html')
display(HTML('networkVisual.html'))