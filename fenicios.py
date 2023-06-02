import time


def main():
    f_map = []
    ports = dict()
    with open("casos/caso20.txt", "r") as f:
        lines = f.readlines()
        print(lines[0])
        lines.remove(lines[0])
        for i, line in enumerate(lines):
            line = line.replace("\n", "")
            n_line = []
            for j, colum in enumerate(line):
                n_line.append(colum)
                if colum == "1":
                    ports["1"] = [i, j]
                if colum == "2":
                    ports["2"] = [i, j]
                if colum == "3":
                    ports["3"] = [i, j]
                if colum == "4":
                    ports["4"] = [i, j]
                if colum == "5":
                    ports["5"] = [i, j]
                if colum == "6":
                    ports["6"] = [i, j]
                if colum == "7":
                    ports["7"] = [i, j]
                if colum == "8":
                    ports["8"] = [i, j]
                if colum == "9":
                    ports["9"] = [i, j]
            f_map.append(n_line)

    print(len(f_map))
    print(len(f_map[0]))
    print(len(ports))
    print(ports)
    print(f_map[ports["1"][0]][ports["1"][1]])
    print(f_map[ports["2"][0]][ports["2"][1]])
    print(f_map[ports["3"][0]][ports["3"][1]])
    print(f_map[ports["4"][0]][ports["4"][1]])
    print(f_map[ports["5"][0]][ports["5"][1]])
    print(f_map[ports["6"][0]][ports["6"][1]])
    print(f_map[ports["7"][0]][ports["7"][1]])
    print(f_map[ports["8"][0]][ports["8"][1]])
    print(f_map[ports["9"][0]][ports["9"][1]])


if __name__ == "__main__":
    main()
