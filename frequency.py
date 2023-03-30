#!/usr/bin/env python3

reeves_text = open("ReevesTale.txt")

ignore_list = ['a', 'the', 'and', 'i', 'of', 'to', 'in', 'was', 'is', 'by', 'is', 'that', 
               'for', 'but', 'no', 'be', 'there', 'on', 'at', 'my', 'it', 'will', 'with',
               'or', 'also', 'thou', 'you', 'we', 'up', 'can', 'which', 'yet', 'do', 'this', 'as',
               'not', 'shall', 'had', 'so', 'now', 'when', 'if', 'am', 'thee']
cleanedReeve = ''
for line in reeves_text:
    line = line.lower()
    if line != "\n":
        for word in line.split(' '):
            word = ''.join(x for x in word if x.isalpha())
            if word != '':
                if word not in ignore_list:
                    cleanedReeve = cleanedReeve + ' '+ word

frequency_dict = {}
for word in cleanedReeve.split(' '):
    if word not in ignore_list:
        if word in frequency_dict:
            frequency_dict[word] = frequency_dict[word] + 1
        else:
            frequency_dict[word] = 1
sorted_dict = sorted(frequency_dict.items(), key=lambda x:x[1])
for item in sorted_dict:
    print(item)
