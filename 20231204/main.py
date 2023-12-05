if __name__ == "__main__":
    lines = open('input.txt', 'r')
    total = 0
    for line in lines:
        _, nums = line.split(':')
        winners, actual = nums.strip().split('|')
        winners = set(winners.strip().split())
        actual = actual.strip().split()
        s = 0
        for a in actual:
            if a in winners:
                s += 1
        total += 0 if s == 0 else pow(2, s - 1)
    print(total)