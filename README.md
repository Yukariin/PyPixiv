# PyPixiv [![Build Status](https://travis-ci.org/Yukariin/PyPixiv.svg)](https://travis-ci.org/Yukariin/PyPixiv)
Unofficial Python API client based on specification extracted from Pixiv Android App v5.0.61

## Requirements.

Python 3.4+ and [requests](https://pypi.python.org/pypi/requests)

## Installation & Usage
### pip install

```sh
pip install git+https://github.com/Yukariin/PyPixiv.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/Yukariin/PyPixiv.git`)

Then import the package:
```python
import pypixiv
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import pypixiv
```

## Getting Started

Please follow the [installation procedure](#installation--usage)

```python
import pypixiv
# create an instance of the API class
api_instance = pypixiv.PixivAppApiClient()

api_response = api_instance.app_info()
print(api_response)
```

## Documentation for API Endpoints

All URIs are relative to *https://app-api.pixiv.net*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*PixivAppApi* | **app_info** | **GET** /v1/application-info/android |
*PixivAppApi* | **emoji** | **GET** /v1/emoji |

## Author

Yukarin
