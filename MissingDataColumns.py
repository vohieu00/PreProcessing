import sys

def MissingDataColumns(data):
    """
    :param data: file name
    :return: list of missing-data colums
    """
    list_col = []
    position = []
    file = open(data, "r")
    if file is None:
        print("Cannot open this file.")
        return
    # get name of columns
    labels = file.readline().split(",")
    # find positions of missing data in each line
    for each in file:
        # get list of index of '' in each line
        line = each.split(',')
        temp = [index for index, value in enumerate(line) if value == '']
        # add position to list
        for i in temp:
            if i not in position:
                position.append(i)

    for i in position:
        list_col.append(labels[i])

    file.close()
    return list_col

if __name__ == '__main__':
    # print(sys.argv)
    if len(sys.argv) < 2:
        print("More argument")
    input_file_name = str(sys.argv[1])
    print(MissingDataColumns(input_file_name))
