# < import modules >
import time
from datetime import datetime

# < import class >
import util.FileUtil as FileUtil
import util.TimeUtil as TimeUtil
import system.Crawling as Crawling
from util.JsonUtil import Json

# < final datas >
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

config = Json("config", '')

def say(message):
    time = datetime.strftime(datetime.now(), DATE_FORMAT)
    print("[CONSOLE] (" + time + ") - " + message)

def initConfig():
    time = datetime.now()

    config.resetData()
    updateCycle = {"day":1}
    config.addData("updateCycle", updateCycle)
    
    str_datetime = datetime.strftime(time, DATE_FORMAT)
    config.addData("updateLast", str_datetime)

    config.saveData()

def checkUpdate():
    currentTime = datetime.now()
    updatedTime = config.getData("updateLast")
    diffDay = TimeUtil.getNowDiffDay(updatedTime, DATE_FORMAT)

    say("Checking Updates...")
    if (diffDay >= config.loadData()['updateCycle']['day']):
        say("Renewal data...")
        try:
            Crawling.run()
        except Exception as error:
            say("Data Crawling Error: " + str(error))
            return

        say("Data Crawling Success...!")
        config.setData("updateLast", datetime.strftime(currentTime, DATE_FORMAT))
        config.saveData()

def main():
    configVaild = FileUtil.isVaild("config.json")

    say("initalizing...")

    if (configVaild == False):
        initConfig()

    say("done...!")

    while (True):
        checkUpdate()
        time.sleep(60)
    
    
if __name__ == '__main__':
    main()