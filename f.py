import math
import time
from queue import PriorityQueue

dr = [-1, +1, 0, 0]  # up down right left
dc = [0, 0, +1, -1]  # up down right left


def find_voyage_cost_a_star(f_map, ports, start, end):
    start = ports[start]
    end = ports[end]
    count = 0
    pq = PriorityQueue()
    pq.put((0, count, tuple(start)))
    came_from = {}
    g_score = {}
    f_score = {}
    for i, row in enumerate(f_map):
        for j, column in enumerate(row):
            g_score[tuple([i, j])] = float("inf")
            f_score[tuple([i, j])] = float("inf")
    g_score[tuple(start)] = 0
    f_score[tuple(start)] = manhattan_distance(start, end)  # heuristic
    open_set_hash = {tuple(start)}

    while not pq.empty():
        current = pq.get()[2]
        open_set_hash.remove(current)

        if current == tuple(end):
            return g_score[current]

        for neighbor in get_neighbors(current[0], current[1], f_map):
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[tuple(neighbor)]:
                came_from[tuple(neighbor)] = current
                g_score[tuple(neighbor)] = temp_g_score
                f_score[tuple(neighbor)] = temp_g_score + manhattan_distance(
                    neighbor, end
                )
                if tuple(neighbor) not in open_set_hash:
                    count += 1
                    pq.put((f_score[tuple(neighbor)], count, tuple(neighbor)))
                    open_set_hash.add(tuple(neighbor))

    return -1


def get_neighbors(row, column, f_map):
    neighbors = []
    r, c = row, column  # row, column
    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]
        if 0 <= rr < len(f_map) and 0 <= cc < len(f_map[0]) and f_map[rr][cc] != "*":
            neighbors.append([rr, cc])
    return neighbors


def manhattan_distance(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


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

    start = time.time()

    total = 0
    currrent = 0
    for i in range(8):
        if currrent == -1:
            print("no hay ruta")
            currrent = find_voyage_cost_a_star(
                f_map,
                ports,
                str(i),
                str(i + 2),
            )
        else:
            currrent = find_voyage_cost_a_star(
                f_map,
                ports,
                str(i + 1),
                str(i + 2),
            )

        if currrent != -1:
            last_valid = i + 2
            total = total + currrent
    total = total + find_voyage_cost_a_star(f_map, ports, str(last_valid), str(1))

    print(total)


if __name__ == "__main__":
    main()
