import sys
import math
import Functions as F

def getMinMax(data):
    value = []
    if F.CheckTypeOfData(data) is True:
        # get min, max values of numeric columns
        data.pop(0)
        temp = list(filter(('').__ne__, data))
        temp = list(map(float, temp))
        value.append(min(temp), max(temp))
    return value

def getMeans(data):
    value = []
    if F.CheckTypeOfData(data) is True:
        # get min, max values of numeric columns
        data.pop(0)
        temp = list(filter(('').__ne__, data))
        temp = list(map(float, temp))
        value.append(sum(temp)/len(temp))
        new_temp = []

        for each in data:
            val = (float(each) - value[0])**2
            new_temp.append(val)
        temp = sum(new_temp)/len(new_temp)
        value.append(math.sqrt(temp))
    return value

def NormalizeData(data, method):
    """
    data_cols is a dictionary which has key is name of columns in data and the value is a list of min-value, max-value
    :param data:
    :param method:
    :return:
    """
    data_cols = dict()
    file = open(data, "r")
    labels = file.readline().strip("\n").split(",")
    file.close()

    for label in labels:
        index = labels.index(label)
        temp = getData(data, labels.index(label))
        if method.lower() == "min-max":
            data_cols[label] = getMinMax(temp)
        else:
            data_cols[label] = getMeans(temp)

    new_file = open("new-"+data, "w")
    file = open(data, "r")

    for line in file:
        temp = line.strip("\n").split(',')
        if method.lower() == "min-max":
            new_line = NormalizeDataByMinMax(temp, data_cols, labels)
        else:
            new_line = NormalizeDataByZscore(temp, data_cols, labels)
        new_line = ','.join(new_line)
        new_file.write(new_line+"\n")
    file.close()
    new_file.close()

def CalNewValueByMinMax(value, data):
    new_max = 1
    new_min = 0
    return ((float(value) - data[0])/(data[1] - data[0]))*(new_max - new_min) + new_min

def getData(file_input, index):
    """"
    Return list of string in each column with given index
    """
    file = open(file_input, "r")
    data = []
    if file is None:
        print("Cannot open this file.")
        return

    for line in file:
        temp = line.split(',')
        data.append(temp[index].rstrip("\n"))

    file.close()
    return data

def NormalizeDataByMinMax(info, data_cols, labels):
    new_data = []

    for each in info:
        if each != '' and F.isNumber(each) is True:
            index = info.index(each)
            label = labels[index]
            each = CalNewValueByMinMax(each, data_cols[label])
        new_data.append(str(each))
    return new_data

def NormalizeDataByZscore(data, data_cols, labels):
    new_data = []

    for each in data:
        if each != '' and F.isNumber(each) is True:
            index = data.index(each)
            label = labels[index]
            each = CalNewValueByZscore(each, data_cols[label])
        new_data.append(str(each))

    return new_data

def CalNewValueByZscore(value, data):
    # population mean = data[0]
    # population standard mean = data[1]
    return (float(value) - data[0])/data[1]

if __name__ == '__main__':
    mode = ["min-max", "z-score"]
    """
    The argument must be in '["min-max", "z-score"] for data
    Example 
            python NormalizeData.py house-prices.csv z-score
    """
    if len(sys.argv) < 3:
        print("More argument")
        pass
    input_file_name = str(sys.argv[1])
    method = str(sys.argv[2])
    if method.lower() not in mode:
        print("Error method")
        pass
    print(NormalizeData(input_file_name, method))

