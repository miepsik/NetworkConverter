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
    for file in files:
        header = []
        data = []
        readFile(file, header, data)
        newData = [[], []]
        distinctEdges = {}
        for i in range(len(data[0])):
            if data[0][i] != data[1][i]:
                if data[0][i] + " " + data[1][i] not in distinctEdges:
                    distinctEdges[data[0][i] + " " + data[1][i]] = 1
                    newData[0].append(data[0][i])
                    newData[1].append(data[1][i])
        saveFile(header, newData, file)


if __name__ == '__main__':
    main()
