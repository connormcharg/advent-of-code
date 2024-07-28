grid = [list(x) for x in open(0).read().splitlines()]
beams = [[0, 0, 1]] # [(i, j, 0/1/2/3)] where 0 is up, 1 is right, 2 is down, 3 is left
gone_through = [[0, 0, 1]]

new_dirs = {
    "/": [1, 0, 3, 2],
    "\\": [3, 2, 1, 0],
    "-": [[1, 3], 1, [1, 3], 3],
    "|": [0, [0, 2], 2, [0, 2]]
}

def advance_beam(beam):
    i, j, direction = beam
    if direction == 0:
        return [i - 1, j, direction]
    elif direction == 1:
        return [i, j + 1, direction]
    elif direction == 2:
        return [i + 1, j, direction]
    elif direction == 3:
        return [i, j - 1, direction]

def get_beams(beam):
    i, j, direction = beam
    dirs = new_dirs[grid[i][j]][direction]
    if isinstance(dirs, list):
        return [[i, j, dirs[0]], [i, j, dirs[1]]]
    return [[i, j, dirs]]

while len(beams) > 0:
    new_beams = []
    for beam in beams:
        i, j, direction = beam
        if grid[i][j] == ".":
            new_beam = advance_beam(beam)
            if 0 <= new_beam[0] < len(grid) and 0 <= new_beam[1] < len(grid[0]):
                if new_beam not in gone_through:
                    new_beams.append(new_beam)
                    gone_through.append(new_beam)
        else:
            temp_beams = get_beams(beam)
            if len(temp_beams) == 2:
                new_beam = advance_beam(temp_beams[0])
                if 0 <= new_beam[0] < len(grid) and 0 <= new_beam[1] < len(grid[0]):
                    if new_beam not in gone_through:
                        new_beams.append(new_beam)
                        gone_through.append(new_beam)
                new_beam = advance_beam(temp_beams[1])
                if 0 <= new_beam[0] < len(grid) and 0 <= new_beam[1] < len(grid[0]):
                    if new_beam not in gone_through:
                        new_beams.append(new_beam)
                        gone_through.append(new_beam)
            else:
                new_beam = advance_beam(temp_beams[0])
                if 0 <= new_beam[0] < len(grid) and 0 <= new_beam[1] < len(grid[0]):
                    if new_beam not in gone_through:
                        new_beams.append(new_beam)
                        gone_through.append(new_beam)
    beams = new_beams

gone_through_coords = []

for beam in gone_through:
    if [beam[0], beam[1]] not in gone_through_coords:
        gone_through_coords.append([beam[0], beam[1]])
