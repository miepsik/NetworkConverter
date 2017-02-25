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
        for i, h in enumerate(header):
            if h == 'A' or h == 'B':
                distinctParamteres = {"NA": 0}
                num = 1
                for p in data[i]:
                    if p not in distinctParamteres:
                        distinctParamteres[p] = num
                        num += 1
                for j in range(len(data[i])):
                    data[i][j] = distinctParamteres[data[i][j]]
            if h == 'X' or h == 'Y':
                for j in range(len(data[i])):
                    data[i][j] = float(data[i][j])
                down = min(data[i])
                up = max(data[i])
                for j in range(len(data[i])):
                    data[i][j] -= down
                    data[i][j] /= (up-down)
                    data[i][j] *= 999
                    data[i][j] += 1
        saveFile(header, data, file)


if __name__ == '__main__':
    main()
