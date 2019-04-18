#! /usr/bin/python

import channellist_pb2
import sys

# Iterates though all channels in the ChannelList and prints info about them.
def ListChannel(channel_list):
  for channel in channel_list.channel:
    print("-"*40)
    print("", channel.c_name)
    print("-"*40)
    if channel.HasField('c_link'):
      print("Link:", channel.c_link)
    if channel.HasField('c_desc'):
      print("Description: *", channel.c_desc.c_desc_1)
      print("             *", channel.c_desc.c_desc_2)
    print("\n")

# Main procedure:  Reads the entire channel list from a file and prints all
#   the information inside.
CHANNEL_LIST_FILE = "CHANNEL_LIST"

if len(sys.argv) != 2:
  print("Using default channellist file:", CHANNEL_LIST_FILE)
else:
  CHANNEL_LIST_FILE = sys.argv[1]

channel_list = channellist_pb2.ChannelList()

# Read the existing channel list.
f = open(CHANNEL_LIST_FILE, "rb")
channel_list.ParseFromString(f.read())
f.close()

ListChannel(channel_list)