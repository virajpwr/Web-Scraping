
# -*- coding:utf8 -*-
# !/usr/bin/env python

import pandas as pd
import os
import urllib

os.chdir('/media/viraj/New Volume/scarping')
weatherst = pd.read_csv('pws.csv')
weatherst.head()

#weatherst.stationid_link.apply(lambda x: x+'#history/s20150525/e20160525/myear').to_csv('test.txt',index=False)
#weatherst.stationid_link.apply(lambda x: x+'#history/s20160413/e20160420/mweek').to_csv('week0420.txt',index=False)
weatherst['Station_id']




for name in weatherst['Station_id']:
    print name
    testfile = urllib.URLopener()
    testfile.retrieve("https://www.wunderground.com/weatherstation/WXDailyHistory.asp?ID="+name
                      +"&day=01&month=01&year=2015&dayend=31&monthend=12&yearend=2015&graphspan=custom&format=0", 'out/'+name+'_allyear.csv') #Scrape weather information from weather underground of year 2015.


