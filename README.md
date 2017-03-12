# YABORMEParser

Yet another BORME Parser.

BORME (Boletin Oficial del Registro Mercantil) is the Official Bulletin of the
Commercial Registry.

* [BORME documents](https://boe.es/diario_borme/)

This program translate BORME PDF files to JSON.

Borme has two Parsers to extract the PDF file data to a json file.

1. Parser: Read PDF files and write raw json files.
2. Parser2: Read raw json files and write process json files.


# Table of Contents

* [Requirements](#requirements)
* [Usage](#usage)
* [Contributing](#contributing)
* [BORMEMining](#bormemining)

# Requirements

YaBORMEParser requires the following to run:

* Python 2.7+
* pdfminer 20140328+
* ply 3.9+

To build the PIP package it is required:

* PyPandoc 1.1.3+

To use the example scripts:

```
apt install parallel bc
```

# Usage

YABORMEParser is easiest to use when installed with pip:

```sh
pip install yabormerparse
```

Then two scripts are installed:

* `yabormeparser1` parse and analyze BORME PDF file. The result is a
  `*.RAW.json` file. It uses PDFMiner.
* `yabormeparser2` transforms a `*.RAW.json` file in a more structured `*.json`
  file. It uses PLY.

## First script

```python
yabormeparser1 -i BORME-A-2009-100-49.pdf
```

We get the most of the times a `BORME-A-2009-100-49.RAW.json` file. But, if some
error happens then we get `BORME-A-2009-100-49.RAW.patch.TMP`. If we get this
latter file we have to:

1. Rename it to `BORME-A-2009-100-49.RAW.patch`.
2. Edit the renamed one in order to solve the error.
3. Exit and execute the parser again with the patch file.

```python
yabormeparser1 -i BORME-A-2009-100-49.pdf -p BORME-A-2009-100-49.RAW.patch
```

Remember to save the file `BORME-A-2009-100-49.RAW.patch` in the code
repository.

To get more options:

```python
yabormeparser1 -h
```

## Second script

The second script is like the first one but:

```python
yabormeparser2 -i BORME-A-2009-100-49.RAW.json
```

And it returns `BORME-A-2009-100-49.json` or `BORME-A-2009-100-49.patch.TMP`.

```python
yabormeparser2 -i  BORME-A-2009-100-49.RAW.json -p  BORME-A-2009-100-49.patch
```

More options:

```python
yabormeparser2 -h
```

# File version

The JSON files have version numbers. If the parser changes the output format or
any data we have to change the version number. This is in order to have
data consistency.

These  version numbers are different from the package version. They have
nothing to do with it.

The first parser version:

In `yabormeparser/parser.py`:

```python
RAW_FILE_VERSION = u'1'
```

In the `*.RAW.json` file:

```js
"raw_version": "1"
```

In `yabormeparser/parser2.py`:

```python
RAW_FILE_VERSION = parser.RAW_FILE_VERSION
# Thousands file version. Represent the file version part corresponding to this
# parser (parser2)
TH_FILE_VERSION = u"7"
# The file version depends on parser one and parser two. It is coded to avoid
# that the parser I change and the parser II does not.
FILE_VERSION = u"%i" % (int(RAW_FILE_VERSION) + 1000 * int(TH_FILE_VERSION))
```

In the `*.json` file:

```js
"raw_version": "1",
"version": "7001"
```

The program, that uses these scripts, must test if the version file is older
than the current one. And if it is it must delete the JSON file and create a
new one.

Put the patch files under `patches/FILE_VERSION_<THE_PARSER2_FILE_VERSION>`.

If you change the version then create a tag in the repository:
`FILE_VERSION_<THE_PARSER2_FILE_VERSION>`, for example, `FILE_VERSION_7001`.


# Contributing

To contribute to YABORMEParser, clone this repo locally and commit your code on
a separate branch.

If you download the code and you don't install the package you can execute the
scripts like:

```
python -m yabormeparser.parser -i examples/BORME-A-2009-100-49.pdf
python -m yabormeparser.parser2 -i examples/BORME-A-2009-100-49.RAW.json
```

## Testing

When you want to correct a bug, first of all, create a test that fail because
of that bug.

When you finish run all python unit tests:

```
python -m unittest discover tests
```

And run all integration tests:

```
mkdir tmp
cp examples/*.pdf tmp
cp examples/*.patch tmp
bin/parser_dir.sh tmp/
```

The last part of the output must be:

```
PDFs 15
JSONs 15
ERRORs 0
```

Now the second parser:

```
bin/parser2_dir.sh tmp/
rm -rf tmp
```

The result must be (or similar):

```
RAWs 15
JSONs 15
ERRORs 0
```

# BORMEMining

BORMEMining is a program that uses YABORMEParser.

BORMEMining:

* downloads BORME PDFs from the BORME web,
* parses BORME PDFs to JSON (in parallel to use all CPUs),
* records state of files, PDFs, and JSONs in a database,
* helps apply patches to problematic PDFs or RAW JSON files...

## BORMEMiningWeb

The database and JSON files of BORMEMining are used for BORMEMiningWeb to give
a Web interface and a REST API.

# Known issues

yabormeparser1 can consume more memory than expected so make sure you have at least 1GB RAM or a SWAP partition:

E.g.:

```
yabormeparser1 -i pdf/2017/03/01/BORME-A-2017-42-08.pdf
```

has 67 pages and uses 350MB+ RAM.


