#!/usr/bin/env python3

text_file = open("parts_of_speech.txt").read()

for line in text_file.split("\n"):
    line_list = []
    name_of_list = ''
    if ',' in line:
        for word in line.split(', '):
            if word not in line_list:
                line_list.append(word)
    else:
        name_of_list = line
    if name_of_list != '':
        print(name_of_list)
    if line_list != []:
        print(line_list)

