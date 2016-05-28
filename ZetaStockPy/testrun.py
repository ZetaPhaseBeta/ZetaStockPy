# -*- coding: utf-8 -*-
"""
Created on Sat May 28 09:01:30 2016

@author: Dave Ho
"""

import pandas as pd

def test_run():
    df = pd.read_csv("data/AAPL.csv")
    print df.head()
    
if __name__ == "__main__":
    test_run()