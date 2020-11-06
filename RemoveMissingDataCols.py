import sys
import MissingDataColumns

def RemoveMissingDataCols(data, proportion):
    """"
    To remove rows having missing data > given proportion
    input: data
    output: new data file
    """
    file = open(data, "r")
    if file is None:
        print("Cannot open this file.")
        return
    # count number of columns
    labels = file.readline().split(',')
    # count number of rows
    rows = 0
    for line in file:
        rows += 1
    pos = []
    # get list of missing data columns
    list_col = MissingDataColumns.MissingDataColumns(data)
    # cal proportion of missing data of every col
    for col in list_col:
        index = labels.index(col)
        count = 0
        file.seek(0, 0)

        for line in file:
            temp = line.split(',')
            if temp[index] == '':
                count += 1

        if count/rows > float(proportion):
            index = labels.index(col)
            pos.append(index)

    # create new file
    new_data_file = "new-" + data
    new_file = open(new_data_file, "w")
    # write new data to another file
    file.seek(0, 0)

    for line in file:
        temp = line.split(',')
        # remove columns missing data
        for col in pos:
            if col != 0:
                temp.remove(''+temp[col])
            else:
                temp.remove(temp[col])
        new_line = ","
        new_line = new_line.join(temp)
        new_file.write(new_line)

    file.close()
    new_file.close()
    return

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("More argument")
    input_file_name = str(sys.argv[1])
    proportion = (sys.argv[2])
    RemoveMissingDataCols(input_file_name, proportion)