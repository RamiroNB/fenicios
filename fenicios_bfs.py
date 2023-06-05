import time

f_map = []
ports = dict()
with open("casos/caso20.txt", "r") as f:
    lines = f.readlines()
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


dr = [-1, +1, 0, 0]  # up down right left
dc = [0, 0, +1, -1]  # up down right left


def find_voyage_cost(
    f_map,
    ports,
    start,
    end,
):
    move_count = 0
    nodes_left_in_layer = 1
    nodes_in_next_layer = 0
    r = len(f_map)
    c = len(f_map[0])
    row_queue = []
    col_queue = []
    reached_end = False
    visited = [[False for _ in range(c)] for _ in range(r)]
    start = ports[start]
    row_queue.append(start[0])
    col_queue.append(start[1])
    visited[start[0]][start[1]] = True
    while len(row_queue) > 0:
        r = row_queue.pop(0)
        c = col_queue.pop(0)
        if f_map[r][c] == end:
            reached_end = True
            break

        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]

            # skip out of bounds locations
            if rr < 0 or cc < 0:
                continue
            if rr >= len(f_map) or cc >= len(f_map[0]):
                continue

            # skip visited locations or blocked cells
            if visited[rr][cc]:
                continue
            if f_map[rr][cc] == "*":
                continue

            row_queue.append(rr)
            col_queue.append(cc)
            visited[rr][cc] = True
            nodes_in_next_layer += 1

        nodes_left_in_layer = nodes_left_in_layer - 1
        if nodes_left_in_layer == 0:
            nodes_left_in_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
            move_count += 1
    if reached_end:
        return move_count
    return -1


start = time.time()
total = 0
currrent = 0
for i in range(8):
    if currrent == -1:
        print("no hay ruta")
        currrent = find_voyage_cost(
            f_map,
            ports,
            str(i),
            str(i + 2),
        )
    else:
        currrent = find_voyage_cost(
            f_map,
            ports,
            str(i + 1),
            str(i + 2),
        )

    if currrent != -1:
        last_valid = i + 2
        total = total + currrent
total = total + find_voyage_cost(f_map, ports, str(last_valid), str(1))
end = time.time()


print(total)
print(end - start)
