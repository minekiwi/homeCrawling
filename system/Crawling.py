# < import modules >
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os 

# < import class >
from util.JsonUtil import Json
import util.TimeUtil as TimeUtil
import util.MongoUtil as MongoUtil
import main as Main

# < final Datas >

# Crawl Data Information
CRAWL_NAME = 'crawl'
CRAWL_LOCATE = 'data/'

# Login Information
load_dotenv()

LOGIN_URL = 'https://www.welfare.mil.kr/content/content.do?m_code=139&forwardName=login.userActionLogin'
USER_ID = os.getenv('userid')
USER_PW = os.getenv('userpw')
LOGIN_DATA = {
    'message': '',
    'type': 'user',
    'goCd': 1,
    'goUrl': '',
    'be_id': '',
    'bm_serial': '',
    'ct': '',
    'pCmV': '',
    'cyber_id': USER_ID,
    'cyber_pw': USER_PW,
}

# Data Crawl Information
CRAWL_URL = 'https://www.welfare.mil.kr/content/content.do?m_code=1222'
CRAWL_FORM_DATA = {
    'forwardName': 'apartment.aptGList'
}

# Database Information
DB_NAME = "test"
COLLECTION_NAME = "subscriptionboq"
COLLECTION = MongoUtil.getCollection(DB_NAME, COLLECTION_NAME)

# Login Function
def login():
    session = requests.Session()
    session.post(LOGIN_URL, data=LOGIN_DATA)
    return session

# Crawl Function
def run():
    session = login()
    
    res = session.post(CRAWL_URL, data=CRAWL_FORM_DATA)
    html = res.text
    content = res.content

    soup = BeautifulSoup(html, 'html.parser')
    subList = soup.find('tbody').get_text().split("\n\n")

    for i in range(0, len(subList)):
        subList[i] = subList[i].replace("\n", "/").replace("[청약자격확인]", "")
    subList.remove('')
    subList.remove('')

    crawlData = Json(CRAWL_NAME, CRAWL_LOCATE)
    crawlData.resetData()

    arr = []

    for sub in subList:
        list = sub.split("/")
        if ('' in list): list.remove('')

        number = list[0]
        locate = list[1]
        name = list[2]
        startDate = list[3]
        finishDate = list[4]
        confirmDate = list[5]

        name = name[1:]
        name = name.replace("(일정미정 추후재공지)", "")
        finishDate = finishDate[0:10] + " " + finishDate[10:13]

        dic = {}
        dic['number'] = number
        dic['locate'] = locate
        dic['name'] = name
        dic['startDate'] = startDate
        dic['finishDate'] = finishDate
        dic['confirmDate'] = confirmDate

        arr.append(dic)

        # Database Update 
        MongoUtil.update(COLLECTION, {"number":number}, {"$set":dic}, True)
        Main.say("Database Update Complete: " + number)
            
    crawlData.addData("data", arr)
    crawlData.saveData()

    # Database Old Data Delete
    for item in COLLECTION.find():
        time = item['confirmDate']
        if TimeUtil.getNowDiffDay(time, '%Y.%m.%d') >= 30:
            MongoUtil.delete(COLLECTION, {"number":item['number']})
            Main.say("Database Delete Complete: " + item['number'])
