# Instructions

1. [For adding channels:](#instructions---channel-contributors)
	1. [Add to README through python.](#setup---install-protobuf)
	2. [Add to queue.](QUEUE.md#queue) 
2. [For open source enthusiasts](#instructions---open-source-enthusiasts)
3. [For developers](#instructions---developers)

## Instructions - Channel Contributors
Intended for those who wish to add channels to this repo.

### Setup - Install protobuf
1. You need to add protobuf library in your python distribution. The following steps will install protobuf module in python. To check if you have protobuf already, use:
```
$ python
>>> import google.protobuf 

# if successful next line is:
>>>
# if failed next line is something like :
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'protobuf'
```

2. Download python release of protobuf ([Click here for all releases](https://github.com/protocolbuffers/protobuf/releases/tag/v3.7.1)) : https://github.com/protocolbuffers/protobuf/releases/download/v3.7.1/protobuf-python-3.7.1.zip

3. To setup protobuf module in python we first need to setup the compiler since we are building from source. After extracting follow:
```
$ cd protobuf-python-3.7.1/protobuf-3.7.1/
$ cd src
$ ./configure
$ make
$ make check
$ sudo make install
$ sudo ldconfig # refresh shared library cache.
```

4. Now it's time to install protobuf in python. Make sure you run the next commands with the correct python interpreter in case you have more than one. Correct i.e. the one you will be using to add channels. Current scripts are in Python 3 compatible only.

```
$ python setup.py build
$ python setup.py test
$ python setup.py install
```

5. Check your installation by running commands in step 1 again.


### Adding a channel to local data file

1. Run the add_channel script using python :
```
cd src
python add_channel.py
```
Use the python interpreter in which protobuf module is installed.

2. Follow the steps in the terminal to enter relevant details.

3. Commit your changes and send PR.

### Display all channels in local data file

1. Run the `display_all_channel.py` script :
```
python display_all_channel.py
```

## Instructions - Open source enthusiasts
Intended for those who would like to finish the scripting items of this repo.

1. Please check the TODO.md
2. Implement any utility that you wish and send a PR.
3. If any more items can be added, modify `TODO.md` or **raise an issue**.


## Instructions - Developers
Intended for those who want to extend this to their own projects.

### Learning basics of protobuf (python):
Link: https://developers.google.com/protocol-buffers/docs/pythontutorial  
Protobuf is Google's standard data exchange format that can be used for data storage in local disk or for transmission over the network.  
As mentioned in Google's docs:
> Protocol buffers are a flexible, efficient, automated mechanism for serializing structured data – think XML, but smaller, faster, and simpler

### Install protobuf
1. Follow the steps of Instructions of Section 1 above.

### Creating python class from proto file
2. Generate the python class from proto file as :
```
protoc -I=. --python_out=. ./channellist.proto

//format: protoc -I=$SRC_DIR --python_out=$DST_DIR $SRC_DIR/addressbook.proto
```

### Using add_channel.py

To specify your own binary data file:
```
python add_channel.py <channel_list_file>

```

