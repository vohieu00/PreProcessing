import sys

def getData(file_input, index):
    filein = open(file_input, "r")
    data = []
    if filein is None:
        print("Can't open file")
        pass
    for line in filein:
        s = line.split(",")
        data.append(s[index].rstrip("\n"))
    filein.close()
    return data

def SplitString(data, seps):
    default_sep = seps[0]
    # we skip seps[0] because that's the default separator
    for sep in seps[1:]:
        data = data.replace(sep, default_sep)
    return [i.strip() for i in data.split(default_sep)]

def SplitOperand(data, seps):
    operand = []
    for symbol in data:
        if symbol in seps:
            operand.append(symbol)
    return operand

def ProcessExpression(labels, in_string, operand):
    datacolumns = {}
    l = []
    l.append("Expression")

    for label in labels:
        index = labels.index(label)
        datacolumns[label] = getData(file_input, index)

    for line in datacolumns[in_string[0]]:
        index = datacolumns[in_string[0]].index(line)
        if index == 0:
            continue
        temp = ""
        empty = "False"
        for opr in operand:
            j = operand.index(opr)
            if datacolumns[in_string[j]][index] != "":

                temp += str(datacolumns[in_string[j]][index]) + opr
                check_zero = temp[-1]
                if check_zero == '/':
                    l.append(0)
            else:
                empty = True
                break

        if datacolumns[in_string[-1]][index] != "" :
            temp += str(datacolumns[in_string[-1]][index])
            if temp[-1] == '0':
                l.append(0)
            else:
                #print(temp)
                l.append(str(eval(temp)))

        if empty == True:
            l.append(0)
            continue

    datacolumns["Expression"] = l
    return datacolumns


def listToString(s):
    # initialize an empty string
    str1 = " "
    # return string
    return (str1.join(s))

if __name__ == '__main__':
    if (len(sys.argv) < 3):
        print("More argument")
        pass
    data = str(sys.argv[2])
    file_input = str(sys.argv[1])
    file = open(file_input, "r")
    labels = file.readline().strip("\n").split(",")

    seps = (' ', '+', '-', '*', '/')
    in_string = []
    in_string = SplitString(data, seps)

    operand = []
    operand = SplitOperand(data, seps)

    dict = {}
    dict = ProcessExpression(labels, in_string, operand)

    fileout = open("new-house-prices.csv", "w")

    labels.append("Expression")

    for line in dict[in_string[0]]:
        index = dict[in_string[0]].index(line)
        for label in labels:
            i = labels.index(label)
            if i != 0:
                fileout.write("," + str(dict[label][index]))
            else:
                fileout.write(str(dict[label][index]))
        fileout.write("\n")
    fileout.close()










