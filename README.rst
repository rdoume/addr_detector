Address Detector
==============================

How to detect if a user query might be an address and requires to launch a map answer.




Project Modules
------------
The  project implements 3 classifiers, using an a la scikit template.

The first classifier is a simple scorer classifier, based on the parsing result of the address parser libpostal (https://github.com/openvenues/libpostal)
According to how the parser manage to work, and which fields are parsed, we make a score and decide if an address or not.

The second classifier is based on the FastText classifier trained on address data. The fasttext makes  an embedding of the differents address it sees and therefore when a new address is submitted if  it's in  a close  spaceto what have been learned.
The classifier is pre-trained, and the Fasttext zip model is store within the package.

The  third classifier is a voting classifier combining the results of the two previous classifiers.


Project Dependencies
------------
####Installation of Postal:
Before you install `Postal` , make sure you have the following prerequisites:
```
sudo apt-get install curl autoconf automake libtool pkg-config
```

Then to install the C library:

```
git clone https://github.com/openvenues/libpostal
cd libpostal
./bootstrap.sh
./configure --datadir=[...some dir with a few GB of space...]
make
sudo make install

# On Linux it's probably a good idea to run
sudo ldconfig
```
#### Installation of FastText
In order to build `fastText`, use the following:

```
$ git clone https://github.com/facebookresearch/fastText.git
$ cd fastText
$ make
```

