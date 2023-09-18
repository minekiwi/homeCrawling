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