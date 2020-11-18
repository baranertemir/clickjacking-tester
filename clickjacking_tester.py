#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 12:27:36 2020

@author: ayca22
"""

import requests
from bs4 import BeautifulSoup

"""
CLICKJACKING TESTER
"""

def checker2(data):
    try:
        if data['X-Frame-Options'] == 'SAMEORIGIN' or data['X-Frame-Options'] == 'DENY':
            print("[-]This site can't be clickjacking.")
    except:
        print("[+]This site can be clickjacking.")

while True:
    url = str(input('URL :'))
    response = requests.get(url)
    response.headers
    data = response.headers
    checker2(data)





        
