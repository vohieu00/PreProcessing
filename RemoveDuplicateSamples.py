import sys

def RemoveDuplicateSamples(data):
    file = open(data, "r+")
    if file is None:
        print("Cannot open this file.")
        return
    # create new file
    new_data_file = "new-" + data
    new_file = open(new_data_file, "w")

    seen_lines = set()

    for line in file:
        if line not in seen_lines:
            new_file.write(line)
            seen_lines.add(line)

    file.close()
    new_file.close()
    return

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("More argument")
    input_file_name = str(sys.argv[1])
    RemoveDuplicateSamples(input_file_name)