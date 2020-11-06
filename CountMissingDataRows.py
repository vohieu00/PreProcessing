import sys

def CountMissingDataRows(data):
    file = open(data, "r+")
    if file is None:
        print("Cannot open this file.")
        return
    labels = file.readline().split(',')
    size = len(labels)
    result = 0

    for line in file:
        line = line.split(',')
        # missing data rows have '''elements in line
        if line.count('') > 0:
            result += 1

    file.close()
    return result

if __name__ == '__main__':
    #print(sys.argv)
    if len(sys.argv) < 2:
        print("More argument")
    input_file_name = str(sys.argv[1])
    print(CountMissingDataRows(input_file_name))