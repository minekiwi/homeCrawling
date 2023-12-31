# < import class >
import util.FileUtil as FileUtil

import json

##
#  Json 파일 관리 기능을 제공하는 클래스
##

class Json:
    def __init__(self, name, locate):
        self.data = {}
        self.locate = locate + name + ".json"
        self.name = name
        if (FileUtil.isVaild(self.locate) == True):
            self.data = self.loadData()

    def addData(self, key, value):
        if (key not in self.data):
            self.data[key] = value
        else:
            self.data[key].append(value)

    def getData(self, key):
        return self.data[key]

    def setData(self, key, value):
        self.data[key] = value

    def resetData(self):
        self.data = {}

    def loadData(self):
        with open(self.locate) as f:
            return json.load(f)

    def saveData(self):
        with open(self.locate, "w") as jsonFile:
            json.dump(self.data, jsonFile, ensure_ascii=False, indent=4, sort_keys=False)