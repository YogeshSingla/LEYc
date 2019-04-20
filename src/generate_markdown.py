#! /usr/bin/python

import channellist_pb2 #protobuf storage of channels
import sys #to get script arguments

PATH='../'
FILENAME = 'README.md'
FILEPATH = PATH + FILENAME


file_contents = """"""
file_header = """
# List of Educational YouTube channels
List of good YouTube channels that are inclined towards education and community building over advertisements and endorsements.
###### Inspiring and Insightful
"""
file_footer = """
### How to contribute?
* SEE [CONTRIBUTING.md](CONTRIBUTING.md#instructions)  
* This `README.md` file is generated using python script: `generate_markdown.py`. Do not edit `README.md` manually. Changes will be overwritten on next execution of `generate_markdown.py`  
***
### Footnotes
>Channels listed here do not rely heavily on advertisements and expect to see very less sponsered content in them.

***
"""

# Iterates though all channels in the ChannelList and adds to a list.
def GenerateMarkdownTable(channel_list):
  channel_content = """"""
  channels_data = []
  serial = 0
  for channel in channel_list.channel:
    serial = serial + 1
    channel_name = channel.c_name
    if channel.HasField('c_link'):
      channel_link = channel.c_link
    else:
      channel_link = ''
    if channel.HasField('c_desc'):
      channel_desc1 = channel.c_desc.c_desc_1
      channel_desc2 = channel.c_desc.c_desc_2
    entry = """|%s.| [%s](%s)|<ul> <li>%s<br><br> <li>%s|
"""%(serial,channel_name,channel_link,channel_desc1,channel_desc2)      
    channel_content = channel_content + entry
  return channel_content

def GenerateMarkdownFile(channel_table):
  channel_table_header = """|S.No.|           Channel            |          Short Description            |
|----|------------------------------|---------------------------------------|
"""
  channel_table = channel_table_header + channel_table
  file_contents = file_header + channel_table + file_footer
  with open(FILEPATH, 'wt') as file:
    file.write(file_contents)

# Main procedure:  Reads the entire channel list from a file and generate a markdown file.
if __name__ == "__main__":
  CHANNEL_LIST_FILE = "CHANNEL_LIST"
  if len(sys.argv) == 2:
    CHANNEL_LIST_FILE = sys.argv[1]

  print("Using channellist file:", CHANNEL_LIST_FILE)

  channel_list = channellist_pb2.ChannelList()

  # Read the existing channel list.
  f = open(CHANNEL_LIST_FILE, "rb")
  channel_list.ParseFromString(f.read())
  f.close()

  # Get channel content in markdown table
  channel_table = GenerateMarkdownTable(channel_list)

  # Generate final markdown file from markdown table
  GenerateMarkdownFile(channel_table)


