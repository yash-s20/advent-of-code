from collections import defaultdict

def map_hand_to_values(hand):
    # maps 2 to A, 3 to B, so on so that all hands are lexico sorted
    char_map = {
        'J': 'a',
        '2': 'b',
        '3': 'c',
        '4': 'd',
        '5': 'e',
        '6': 'f',
        '7': 'g',
        '8': 'h',
        '9': 'i',
        'T': 'j',
        'Q': 'k',
        'K': 'l',
        'A': 'm'
    }
    s = ""
    for c in hand:
        s += char_map[c]
    return s

def get_score_of_hand(hand: str):
    num_j = hand.count('J')
    char_to_count = defaultdict(lambda: 0)
    for c in hand:
        char_to_count[c] += 1
    char_to_count['J'] = 0
    max_count = max(char_to_count.values())
    for k, v in char_to_count.items():
        if max_count == v:
            char_to_count[k] = v + num_j
            break

    count_to_freq = defaultdict(lambda: 0)
    for n in char_to_count.values():
        count_to_freq[n] += 1
    if count_to_freq[5]:
        return 7 # five of a kind
    if count_to_freq[4]:
        return 6 # four of a kind
    if count_to_freq[3] == 1 and count_to_freq[2] == 1:
        return 5 # full house
    if count_to_freq[3] == 1:
        return 4 # three of a kind
    if count_to_freq[2] == 2:
        return 3 # two pair
    if count_to_freq[2] == 1:
        return 2 # one pair
    return 1 # high card
        

if __name__ == "__main__":
    lines = open('input.txt', 'r').readlines()
    hands = []
    bids = []
    for line in lines:
        hand, bid = line.strip().split()
        bids.append(int(bid))
        hands.append(hand)
    total = 0
    hands = [(get_score_of_hand(hand), map_hand_to_values(hand), bid) for hand, bid in zip(hands, bids)]
    hands.sort()
    for (i, (_, h, b)) in enumerate(hands):
        print(h)
        total += (i + 1) * b
    print(total)