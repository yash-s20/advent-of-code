from functools import reduce

def game_power(rounds: str):
    cubes = {'red': 0, 'blue': 0, "green": 0}
    for round in rounds:
        for sample in round.split(','):
            n, c = sample.split()
            n = int(n)
            cubes[c] = max(cubes[c], n)
    return reduce(lambda y, x: y * x, cubes.values(), 1)

if __name__ == "__main__":
    lines = open('input.txt', 'r').readlines()
    s = 0
    for line in lines:
        line = line.strip()
        game, rounds = line.split(':')
        *_, game = game.split(' ')
        game = int(game)
        rounds = rounds.split(';')
        s += game_power(rounds)
    print(s)