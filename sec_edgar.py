# tool searching CIK or Series ID on SEC based on mutual funds symbols 
import re
import urllib
import _pickle 
import requests
import pandas as pd
import sys
from _pickle import dump
from requests import get
def getCIKs(TICKERS):
    for SYMBOL in TICKERS:

        URL = 'https://www.sec.gov/cgi-bin/series?ticker='+SYMBOL+'&CIK=&sc=companyseries&type=N-PX&Find=Search'
        #print(URL)
        Page = urllib.request.urlopen(URL).read().decode('utf-8')
        #print(Page)
        CIK_RE = re.findall(r'CIK=(S\d{9})', Page) or "NULL"
        print(CIK_RE[0])
tickers_sample = pd.read_csv("LIST.csv") # PATH TO custom list of symbols
#print(tickers_sample)
#print(tickers_sample.SYMBOL)
symbols_list = list(tickers_sample["SYMBOL"])
#print(symbols_list)
#getCIKs(symbols_list)
getCIKs(symbols_list)
#print(CIK_samples)
#CIK_samples.to_csv(r'SAMPLES.CSV') # PATH TO SAVE DEST
