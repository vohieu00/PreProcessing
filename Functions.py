def isNumber(value):
    if value.isdigit():
        return True
    temp = value.replace('.', '')
    if temp.isdigit():
        return True
    return False

def Mode(data):
    return max(set(data), key = data.count)

def Mean(data):
    return float(sum(data) / len(data))

def Median(data):
    data.sort()
    pos = int(len(data) / 2)
    if len(data) % 2 == 0:
        return float((data[pos - 1] + data[pos]) / 2)
    return float(data[pos])
def CheckTypeOfData(data):
    """
    If data is numeric, return true
    If data is not numeric or null, return false
    """
    index = 1
    while(True):
        if data[index] != '':
           check = isNumber(data[index])
           return check

    return False
    