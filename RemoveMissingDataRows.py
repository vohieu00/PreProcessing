import sys

def RemoveMissingDataRows(data, proportion):
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
    size = len(labels)
    #create a new file
    new_data_file = "new-" + data
    new_file = open(new_data_file, "w")
    file.seek(0, 0)
    # write data to new file
    for line in file:
        temp = line.split(',')
        p = temp.count('')/size
        if p < float(proportion):
            new_file.write(line)

    file.close()
    new_file.close()
    return

if __name__ == '__main__':
    #print(sys.argv)
    if len(sys.argv) < 3:
        print("More argument")
    input_file_name = str(sys.argv[1])
    proportion = (sys.argv[2])
    RemoveMissingDataRows(input_file_name, proportion)