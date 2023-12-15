import numpy as np


topleft = ord('F')
btmleft = ord('L')
btmrght = ord('J')
toprght = ord('7')
start = ord('S')
horzntl = ord('-')
verticl = ord('|')

def find_in_or_out(grid, x, y, pipes_in_path):
    is_out = True
    while y >= 0:
        if grid[x, y] in pipes_in_path:
            is_out = not is_out
        y -= 1
    return is_out

def goright(x, y):
    return x, y + 1

def goleft(x, y):
    return x, y - 1

def godown(x, y):
    return x + 1, y

def goup(x, y):
    return x - 1, y

def outofbounds(x, y, N, M):
    return x < 0 or y < 0 or x >= N or y >= M

def validright(grid, x, y):
    return (grid[x, y] == start or
            grid[x, y] == horzntl or
            grid[x, y] == btmrght or
            grid[x, y] == toprght)

def validleft(grid, x, y):
    return (grid[x, y] == start or 
            grid[x, y] == horzntl or
            grid[x, y] == topleft or
            grid[x ,y] == btmleft)


def validup(grid, x, y):
    return (grid[x, y] == start or 
            grid[x, y] == verticl or
            grid[x, y] == topleft or
            grid[x ,y] == toprght)


def validdown(grid, x, y):
    return (grid[x, y] == start or 
            grid[x, y] == verticl or
            grid[x, y] == btmleft or
            grid[x ,y] == btmrght)


def complete_loop(grid, start_pos, path=None, direction=None):
    if path is None:
        visited = {start_pos}
        path = [start_pos]
    else:
        path = path.copy()
        visited = set(path)
    N, M = grid.shape
    pos = path[-1]
    while True:
        if grid[pos] == topleft:
            if direction == 'l':
                direction = 'd'
                pos = godown(*pos)
            elif direction == 'u':
                direction = 'r'
                pos = goright(*pos)
            else:
                return False, []
            if outofbounds(*pos, N, M):
                return False, []
        elif grid[pos] == toprght:
            if direction == 'r':
                direction = 'd'
                pos = godown(*pos)
            elif direction == 'u':
                direction = 'l'
                pos = goleft(*pos)
            else:
                return False, []
            if outofbounds(*pos, N, M):
                return False, []
        elif grid[pos] == btmrght:
            if direction == 'd':
                direction = 'l'
                pos = goleft(*pos)
            elif direction == 'r':
                direction = 'u'
                pos = goup(*pos)
            else:
                return False, []
            if outofbounds(*pos, N, M):
                return False, []
        elif grid[pos] == btmleft:
            if direction == 'd':
                direction = 'r'
                pos = goright(*pos)
            elif direction == 'l':
                direction = 'u'
                pos = goup(*pos)
            else:
                return False, []
            if outofbounds(*pos, N, M):
                return False, []
        elif grid[pos] == start:
            # check every direction except the one coming from
            # direction is None, starting here
            new_pos = goup(*pos)
            b, full_path = complete_loop(grid, new_pos, path + [new_pos], 'u')
            if b:
                return True, full_path
            new_pos = godown(*pos)
            b, full_path = complete_loop(grid, start_pos, path + [new_pos], 'd')
            if b:
                return True, full_path
            new_pos = goright(*pos)
            b, full_path = complete_loop(grid, start_pos, path + [new_pos], 'r')
            if b: 
                return True, full_path
            new_pos = goleft(*pos)
            print(new_pos, direction)
            b, full_path = complete_loop(grid, start_pos, path + [new_pos], 'l')
            if b:
                return True, full_path
            # No path from S
            return False, []
        elif grid[pos] == horzntl:
            if direction == 'u' or direction == 'd':
                return False, []
            if direction == 'l':
                pos = goleft(*pos)
                if outofbounds(*pos, N, M):
                    return False, []
            if direction == 'r':
                pos = goright(*pos)
                if outofbounds(*pos, N, M):
                    return False, []
        elif grid[pos] == verticl:
            if direction == 'l' or direction == 'r':
                return False, []
            if direction == 'u':
                pos = goup(*pos)
                if outofbounds(*pos, N, M) or (not validup(grid, *pos)):
                    return False, []
            if direction == 'd':
                pos = godown(*pos)
                if outofbounds(*pos, N, M) or (not validdown(grid, *pos)):
                    return False, []
        else:
            return False, []
        if pos in visited and pos == start_pos:
            return True, path
        if pos in visited:
            # loop but not complete, intersects in the middle
            return False, []
        path.append(pos)
        visited.add(pos)

dot = ord('.')

if __name__ == "__main__":
    lines = open('sample_input.txt', 'r').readlines()
    lines = list(lines)
    N = len(lines)
    M = len(lines[0])
    x = np.ndarray((N, M), dtype=np.uint8)
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            x[i][j] = ord(char)
    start_poses = np.where(x == start)
    # print(start_poses)
    for pos in zip(*start_poses):
        # print(pos)
        b, path = complete_loop(x, pos)
        if b:
            print(path)
            print(len(path) // 2)
    pipes_in_path = set(path)
    for i in range(N):
        for j in range(M):
            if (i, j) not in pipes_in_path:
                x[i, j] = ord('.')
    for i in range(N):
        for j in range(M):
            print(chr(x[i, j]), end="")
        print()
    out = ord('O')
    ins = ord('I')
    for i in range(N):
        for j in range(M):
            # if x[i, j] == out or x[i, j] == ins:
                # continue
            if (i, j) in pipes_in_path:
                continue
            is_out = find_in_or_out(x, i, j, pipes_in_path)
            if is_out:
                x[i, j] = out
            else:
                x[i, j] = ins
    for i in range(N):
        for j in range(M):
            print(chr(x[i, j]), end="")
        print()
    