#! /usr/bin/python

import channellist_pb2
import sys

# This function fills in a Person message based on user input.
def AddChannel(channel):
  channel.c_name = input("Enter channel name: ")
  c_link = input("Enter YouTube link: ")
  if c_link != "":
    channel.c_link = c_link

  desc1 = input("Enter description (#1 of 2)(key areas of channel, what is it about): ")
  if desc1 != "":
    channel.c_desc.c_desc_1 = desc1
    

  desc2 = input("Enter description (#2 of 2)(length and type of videos or any other USP): ")
  if desc2 != "":
    channel.c_desc.c_desc_2 = desc2

# Main procedure:  Reads the entire channle list from a file,
#   adds one channel based on user input, then writes it back out to the same
#   file.
CHANNEL_LIST_FILE = "CHANNEL_LIST"

if len(sys.argv) != 2:
  print("Using default channellist file:", CHANNEL_LIST_FILE)
else:
  CHANNEL_LIST_FILE = sys.argv[1]

channel_list = channellist_pb2.ChannelList()

# Read the existing channel list.
try:
  f = open(CHANNEL_LIST_FILE, "rb")
  channel_list.ParseFromString(f.read())
  f.close()
except IOError:
  print(CHANNEL_LIST_FILE + ": Could not open file.  Creating a new one.")

# Add an channel.
AddChannel(channel_list.channel.add())

# Write the new channel list back to disk.
f = open(CHANNEL_LIST_FILE, "wb")
f.write(channel_list.SerializeToString())
f.close()