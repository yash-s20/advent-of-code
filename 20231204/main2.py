if __name__ == "__main__":
    lines = open('input.txt', 'r')
    total = 0
    win_count = []
    for line in lines:
        _, nums = line.split(':')
        winners, actual = nums.strip().split('|')
        winners = set(winners.strip().split())
        actual = actual.strip().split()
        w = 0
        for a in actual:
            if a in winners:
                w += 1
        win_count.append(w)
    copies = [1] * len(win_count)
    total = 0
    for idx, copy in enumerate(copies):
        print(idx, copy)
        wins = win_count[idx]
        total += copy
        for j in range(wins):
            copies[idx + j + 1] += copy
    print(total)