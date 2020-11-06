import sys
import MissingDataColumns as mdc
import Functions as F

def FillMissingNumericData(data, method, new_data):
    file = open(data, "r")
    if file is None:
        print("Cannot open this file.")
        return
    labels = file.readline().split(',')
    list_col = mdc.MissingDataColumns(data)
    col_val = dict()
    mode = 0
    if method.lower() == "median":
        mode = 1
    # calculate mean of missing data cols
    for col in list_col:
        index = labels.index(col)
        # get data in col
        list_data = []
        file.seek(0, 0)

        for line in file:
            temp = line.split(',')
            # check if data is number
            if temp[index] != '':
                if F.isNumber(temp[index]) is True:
                    list_data.append(float(temp[index]))
                else:
                    break

        if len(list_data) > 0:
            if mode == 0: # mean method
                col_val[col] = F.Mean(list_data)
            elif mode == 1: # median method
                col_val[col] = F.Median(list_data)

        list_data.clear()

    # create new file
    new_file = open(new_data, "w")

    file.seek(0, 0)
    for line in file:
        temp = line.split(',')
        # fill missing data
        for col in col_val.keys():
            index = labels.index(col)
            if temp[index] == '':
                temp[index] = col_val[col]

        new_line = ","
        new_line = new_line.join([str(each) for each in temp])
        new_file.write(new_line)

    new_file.close()
    file.close()
    return

def FillMissingCategoricalData(data, new_data):
    file = open(data, "r")
    if file is None:
        print("Cannot open this file.")
        return
    labels = file.readline().split(',')
    list_col = mdc.MissingDataColumns(data)
    col_val = dict()
    # calculate mean of missing data cols
    for col in list_col:
        index = labels.index(col)
        # get data in col
        list_data = []
        file.seek(0, 0)

        for line in file:
            temp = line.split(',')
            # check if data is categorical
            if temp[index] != '':
                if F.isNumber(temp[index]) is False:
                    list_data.append(temp[index])
                else:
                    break


        if len(list_data) > 0:
            col_val[col] = F.Mode(list_data)
        list_data.clear()

    # create new file
    new_file = open(new_data, "w")
    file.seek(0, 0)

    for line in file:
        temp = line.split(',')
        # fill missing data
        for col in col_val.keys():
            index = labels.index(col)
            if temp[index] == '':
                temp[index] = col_val[col]

        new_line = ","
        new_line = new_line.join([str(each) for each in temp])
        new_file.write(new_line)

    new_file.close()
    file.close()
    return




def FillMissingData(data, method):
    """
    :param data: a file missing data
    :param method: string
    :param result: a new file
    :return:
    """
    FillMissingNumericData(data, method, "1st_version-"+data)
    FillMissingCategoricalData("1st_version-"+data, "new-"+data)
    return

if __name__ == '__main__':
    """
    The argument must be in '["mean" , "median"] for numeric data
    Example 
            python FillMissingData.py house-prices.csv mean
    """
    if len(sys.argv) < 3:
        print("More argument")
    input_file_name = str(sys.argv[1])
    method = str(sys.argv[2])
    FillMissingData(input_file_name, method)

