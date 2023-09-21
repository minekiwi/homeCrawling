# < import modules >
import time
from datetime import datetime
from datetime import date

# < import class >
import util.DataManager as DataManager
import system.Crawling as Crawling
from util.JsonFile import Json

# < final datas >
DATE_FORMAT = '%Y-%m-%d %Hh'

config = Json("config", '')

def initConfig():
    time = datetime.now()

    config.resetData()
    updateCycle = {"day":7}
    config.addData("updateCycle", updateCycle)
    
    str_datetime = datetime.strftime(time, DATE_FORMAT)
    config.addData("updateLast", str_datetime)

    config.saveData()

def readConfig(read):
    return config.loadData()[read]

def checkUpdate():
    currentTime = datetime.now()
    updatedTime = readConfig("updateLast") 
    updatedTime = time.mktime(datetime.strptime(updatedTime, DATE_FORMAT).timetuple())
    updatedTime = datetime.fromtimestamp(updatedTime)
    diffDay = (currentTime - updatedTime).days

    if (diffDay >= config.loadData()['updateCycle']['day']):
        print("renewal crawl data...")

def main():
    configVaild = DataManager.isVaild("config.json")

    print("initalizing...")

    if (configVaild == False):
        initConfig()

    print("done...!")
    
    
if __name__ == '__main__':
    main()