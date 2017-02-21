import os
import urllib.request
import requests

def get_txt(file, sep='\n'):
    with open(file) as f:
        return [x.strip() for x in f.read().split(sep) if x.strip() != '']


def download_file(url, filename):
    if os.path.exists(filename):
        return
    urllib.request.urlretrieve(url, filename=filename)


def get_url(url):
    return requests.get(url)
