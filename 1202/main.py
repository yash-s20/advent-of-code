cubes = {'red': 12,
         'green': 13,
         'blue': 14
        }

def round_check(round: str):
    for sample in round.split(','):
        n, c = sample.split()
        n = int(n)
        if cubes[c] < n:
            return False
    return True


if __name__ == "__main__":
    lines = open('input.txt', 'r').readlines()
    s = 0
    for line in lines:
        line = line.strip()
        game, rounds = line.split(':')
        *_, game = game.split(' ')
        game = int(game)
        rounds = rounds.split(';')
        if all([round_check(r) for r in rounds]):
            s += game
    print(s)