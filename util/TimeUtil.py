# < import modules >
import time
from datetime import datetime
from datetime import date

##
#  시간 관련 기능을 제공하는 클래스
##

# < final datas >
CRAWL_DATE_FORMAT = '%Y-%m-%d'

def getNowDiffDay(time):
    currentTime = datetime.now()
    diffDay = (currentTime - time).days
    return diffDay

def getNowDiffDay(date, format):
    currentTime = datetime.now()
    compareTime = time.mktime(datetime.strptime(date, format).timetuple())
    compareTime = datetime.fromtimestamp(compareTime)
    diffDay = (currentTime - compareTime).days
    return diffDay