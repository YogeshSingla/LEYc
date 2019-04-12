#!/usr/bin/python
import cgi
import io
import csv
import os


PATH='/home/kirito/TODO/LEYc/'
FILENAME = 'readme.md'
FILEPATH = PATH + FILENAME


file_contents = """"""

file_header = """
# List of Educational YouTube channels
### Mathematics and Computing Science
###### Inspiring and Insightful
"""

file_footer = """
### How to contribute?
>Fork this repo and add the channels you find and send a PR.

***
### Footnotes
channels listed here do not rely heavily on advertisements and expect to see very less sponsered content in them.

***
"""

channels_data = [['3Blue1Brown','https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw','  Videos on intermediate level maths concepts like differentiation, curl, eigen values offering valuable insights.','Generally, longer videos of around 20-25 minutes from a very humble creator with really sweet voice.'],
['LeiosOS','https://www.youtube.com/channel/UCd0dc7kQA1FUpJ76o1EjLqQ',' 2-3 minutes videos broadly ranging from calculus to algorithms.','Appreciated for sheer interest in the subject and his passion visible in his videos.'],
['Art of the Problem','https://www.youtube.com/channel/UCotwjyJnb-4KW7bmsOoLfkg','Deceptively named, the channel focuses on computer science and it\'s history. It also covers Information Theory in a insight revealing manner. ','Videos range from 2 to 10 mins, averaging around 5 mins.'],
['Welch Labs','https://www.youtube.com/user/Taylorns34','Videos on machine learning, imaginery numbers and music. Takes an inquisitive viewpoint over plain theory regurgitation.','Short videos that leave you thinking at the end. Introductory series on machine learning titled <b>"Learning to See"</b> highly recommended. ']]


channel_content = """|S.No.|           Channel            |          Short Description            |
|----|------------------------------|---------------------------------------|
"""

for i in range(4):
	serial = i + 1
	channel_name = channels_data[i][0]
	channel_link = channels_data[i][1]
	channel_desc1 = channels_data[i][2]
	channel_desc2 = channels_data[i][3]
	entry = """|%s.| [%s](%s)|<ul> <li>%s<br><br> <li>%s|
"""%(serial,channel_name,channel_link,channel_desc1,channel_desc2)

	channel_content = channel_content + entry

file_contents = file_header + channel_content + file_footer

if (os.access(PATH, os.R_OK)):
	with open(FILEPATH, 'wt') as file:
		file.write(file_contents)
else:
	print("Error: File or folder access not available")



