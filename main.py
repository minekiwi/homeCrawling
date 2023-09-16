# < import modules >
import configparser
from datetime import datetime

# < import class >
import util.DataManager as DataManager

def initConfig():
    time = datetime.now()

    config = configparser.ConfigParser()
    config = {}
    config['update'] = time.strftime('%Y-%m-%d %H:%M:%S')

    with open('config.ini', 'w', encoding='utf-8') as configfile:
        config.write(configfile)

def readConfig(read):
    config = configparser.ConfigParser()    
    config.read('config.ini', encoding='utf-8') 

    return config[read]

def main():
    config = DataManager.read("config")
    crawlTime = datetime.now()
    if (config == False):
        initConfig()
    
if __name__ == '__main__':
    main()