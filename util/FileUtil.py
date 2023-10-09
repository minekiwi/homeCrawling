##
#  파일 관련 기능을 제공하는 클래스
##

def isVaild(name):
    try:
        file = open(name, 'r')
        return True
    except:
        return False

def write(name, data):
    f = open(name, 'a')
    f.write(data)
    f.close()

def read(name):
    try:
        file = open(name, 'r')
        Lines = file.readlines()
        return Lines
    except:
        return False

def new(name):
    f = open(name, 'w')
    f.close()