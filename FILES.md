
# File Tree

```
.
├── FILES.md : This file
├── INSTRUCTIONS.md : Steps for contributors to this repo.
├── QUEUE.md : List of channels to be added to readme by python script in case the contributor couldn't run python script.
├── README.md : Main list
├── src
│   ├── add_channel.py : Script to be used to add channels to CHANNEL_LIST binary data file.
│   ├── CHANNEL_LIST : Binary file in protobuf format for storing channels.
│   ├── channellist_pb2.py : Python class file generated from .proto file by protobuf module in python.
│   ├── channellist.proto : Format of message to be stored in protobuf binary data file. (user defined)
│   ├── display_all_channel.py : Debug script to show all channels in CHANNEL_LIST
│   ├── generate_markdown.py : Script to generate the README.md file from CHANNEL_LIST
└── TODO.md : Checklist for tasks for this repo.

```