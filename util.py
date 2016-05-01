#!/usr/bin/python2

import xbmc
import os
import time
import urllib
import urllib2
from bs4 import BeautifulSoup
import xmltodict

import player_config

def is_file_valid(cache_file, timeout):
    if os.path.isfile(cache_file):
        modified_time = os.path.getmtime(cache_file)
        current_time = time.time()
        return current_time - modified_time < timeout
    return False


def fetch_file(url, cache_file):
    urllib.urlretrieve(url, cache_file)

def load_file(cache_file):
    return open(cache_file, 'r')

def get_url_as_xml_soup_cache(url, cache_file, timeout = 1):
    if not is_file_valid(cache_file, timeout):
        xbmc.log('ESPN3: Fetching config file %s from %s' % (cache_file, url))
        fetch_file(url, cache_file)
    else:
        xbmc.log('ESPN3: Using cache %s for %s' % (url, cache_file))
    config_file = load_file(cache_file)
    config_data = config_file.read()
    config_file.close()
    xbmc.log('ESPN3: Start soup')
    #config_soup = BeautifulSoup(config_data, 'html.parser')
    config_soup = xmltodict.parse(config_data)
    xbmc.log('ESPN3: End soup')
    return config_soup

def get_url_as_xml_soup(url):
    config_data = urllib2.urlopen(url).read()
    config_soup = BeautifulSoup(config_data, 'html.parser')
    return config_soup
