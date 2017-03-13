import sys


def main():
    file = sys.argv[1]
    matrix = []
    first = True
    with open(file) as f:
        for i, line in enumerate(f):
            for x in line:
                if x not in (" ", ",", ";", "\n"):
                    if first:
                        matrix.append([])
                    matrix[i].append(int(x))
            first = False
    print(matrix)
    lines = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                lines.append(str(i+1)+";"+str(j+1))
    print(lines)
    with open(file + ".edges", "w") as f:
        f.write("From;To\n")
        for row in lines:
            f.write(row + "\n")


if __name__ == '__main__':
    main()
