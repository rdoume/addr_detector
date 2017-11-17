# Address Detector

How to detect if a user query might be an address and requires to launch
a map answer.

## Project Modules

The project implements 3 classifiers, using an a la scikit template.

The first classifier is a simple scorer classifier, based on the parsing
result of the address parser libpostal
(https://github.com/openvenues/libpostal) According to how the parser
manage to work, and which fields are parsed, we make a score and decide
if an address or not.

The second classifier is based on the FastText classifier trained on
address data. The fasttext makes an embedding of the differents address
it sees and therefore when a new address is submitted if it’s in a close
spaceto what have been learned. The classifier is pre-trained, and the
Fasttext zip model is store within the package.

The third classifier is a voting classifier combining the results of the
two previous classifiers.

## Project Dependencies

#### Installation of Postal: Before you install `Postal` , make sure
you have the following prerequisites:

    sudo apt-get install curl autoconf automake libtool pkg-config

Then to install the C library:

    git clone https://github.com/openvenues/libpostal
    cd libpostal
    ./bootstrap.sh
    ./configure --datadir=[...some dir with a few GB of space...]
    make
    sudo make install

    # On Linux it's probably a good idea to run
    sudo ldconfig

#### Installation of FastText

In order to build `fastText`, use the following:

    $ git clone https://github.com/facebookresearch/fastText.git
    $ cd fastText
    $ make

#### Installation of Package
The previous step must have been installed before.

Package is on the Pipy :
pip install addr_detector

Or directly after forking this one, run `pip install -r requirements.txt`

## Examples:




```python
from addr_detector.Fasttext_clf import Fasttext_clf
from addr_detector.Postal_clf import Postal_clf
```


```python
clf1 = Fasttext_clf()
clf2 = Postal_clf()

```


```python
addresse =  ['7 rue Spontini Paris']
print(clf1.predict(addresse))
print(clf2.predict(addresse))

```

    [True]
    [True]



```python
addresses= ['7 rue Spontini Paris', '27 rue de l université Paris','Comment se faire cuire un oeuf','Google\n']

print(clf1.predict(addresses))
print(clf2.predict(addresses))
```

    [True, True, False, False]
    [True, True, False, False]
