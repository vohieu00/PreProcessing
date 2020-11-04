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
        value.append(min(temp))
        value.append(max(temp))
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

def NormalizeData(data, method,attribute):
    """
    data_cols is a dictionary which has key is name of columns in data and the value is a list of min-value, max-value
    :param data:
    :param method:
    :return:
    """
    data_cols = dict()
    file = open(data, "r")
    labels = file.readline().strip("\n").split(",")
    if attribute not in labels:
        print("The attribute doesnot exist in data")
        return
    file.close()

    index = labels.index(attribute)
    temp = getData(data, labels.index(attribute))
    # print(temp)
    if method.lower() == "min-max":
        data_cols[attribute] = getMinMax(temp)
    else:
        data_cols[attribute] = getMeans(temp)
    # print(data_cols[attribute])
    new_file = open("new-"+data, "w")
    file = open(data, "r")

    for line in file:
        temp = line.strip("\n").split(',')
        if method.lower() == "min-max":
            new_line = NormalizeDataByMinMax(temp, data_cols, attribute, index)
        else:
            new_line = NormalizeDataByZscore(temp, data_cols, attribute, index)
        # print(new_line)
        new_line = ','.join(new_line)
        new_file.write(new_line+"\n")
    file.close()
    new_file.close()

def CalNewValueByMinMax(value, data):
    new_max = 1
    new_min = 0
    temp = ((float(value) - data[0])/(data[1] - data[0]))*(new_max - new_min) + new_min
    return temp

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

def NormalizeDataByMinMax(info, data_cols, label, index):
    # info : a list of word in line
    # data_cols contains data to normalize
    # label is attribute need normalize
    # print(info)
    new_data = info
    if info[index] != '' and F.isNumber(info[index]) is True:
        new_val = CalNewValueByMinMax(info[index], data_cols[label])
        new_data[index] = str(new_val)
    # print(new_data)
    return new_data

def NormalizeDataByZscore(info, data_cols, label, index):
    new_data = info
    if info[index] != '' and F.isNumber(info) is True:
        new_val = CalNewValueByZscore(info[index], data_cols[label])
        new_data[index] = new_val
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
            python NormalizeData.py house-prices.csv Area z-score
    """
    if len(sys.argv) < 4:
        print("More argument")
        pass
    input_file_name = str(sys.argv[1])
    attribute = str(sys.argv[2])
    method = str(sys.argv[3])
    if method.lower() not in mode:
        print("Error method")
        pass
    NormalizeData(input_file_name, method, attribute)

