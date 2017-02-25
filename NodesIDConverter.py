import csv
import sys


def readFile(file, header, data):
    with open(file) as f:
        line = f.readline()
        if line.find(";") != -1:
            delimiter = ";"
        else:
            delimiter = ","
        f.seek(0)
        reader = csv.reader(f, delimiter=delimiter)
        h = True
        for row in reader:
            if h:
                for x in row:
                    header.append(x)
                    data.append([])
                h = False
            else:
                for i, x in enumerate(row):
                    data[i].append(x)


def saveFile(header, data, file):
    with open(file, "w") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(header)
        data = zip(*data)
        for row in data:
            writer.writerow(row)


def main():
    files = sys.argv[1:]
    newID = {}
    for i, file in enumerate(files):
        header = []
        data = []
        readFile(file, header, data)
        if i == 0:
            num = 1
            for p in data[0]:
                if p not in newID:
                    newID[p] = num
                    num += 1
            for j in range(len(data[0])):
                data[0][j] = newID[data[0][j]]
        else:
            for j in range(len(data)):
                for l in range(len(data[j])):
                    data[j][l] = newID[data[j][l]]
        saveFile(header, data, file)


if __name__ == '__main__':
    main()
