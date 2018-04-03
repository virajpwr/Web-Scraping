import pandas as pd
import os
os.chdir('/media/viraj/New Volume/Work/DWBI/tree/scarping')
nyc=pd.read_csv('pws.csv')
nyc.head()
#nyc.stationid_link.apply(lambda x: x+'#history/s20150525/e20160525/myear').to_csv('test.txt',index=False)
#nyc.stationid_link.apply(lambda x: x+'#history/s20160413/e20160420/mweek').to_csv('week0420.txt',index=False)
nyc['Station_id']
import urllib
import pandas as pd
for name in nyc['Station_id']:
    print name
    testfile = urllib.URLopener()
    testfile.retrieve("https://www.wunderground.com/weatherstation/WXDailyHistory.asp?ID="+name
                      +"&day=01&month=01&year=2015&dayend=31&monthend=12&yearend=2015&graphspan=custom&format=0", 'out/'+name+'_allyear.csv')


