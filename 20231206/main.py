def make_list(x):
    _, x = x.split(':')
    x = x.strip().split()
    x = [int(t) for t in x]
    return x

def get_dist(t, T):
    return t * (T - t)

if __name__ == "__main__":
    lines = open('input.txt', 'r').readlines()
    prod = 1
    time, dist = lines
    time = make_list(time)
    dist = make_list(dist)
    for t, d in zip(time, dist):
        max_time = t // 2
        max_dist = get_dist(max_time, t)
        if max_dist < d:
            print(0)
            exit(0)
        new_min = max_time // 2
        left_bound = 0
        right_bound = max_time
        while (new_min != left_bound) and (new_min != right_bound):
            if get_dist(new_min, t) <= d:
                left_bound = new_min
                new_min = (left_bound + right_bound) // 2
            elif get_dist(new_min, t) > d:
                right_bound = new_min
                new_min = (left_bound + right_bound) // 2
        while get_dist(new_min, t) <= d:
            new_min += 1
        num_ways = (t - 2 * new_min) + 1
        print(new_min, num_ways)
        prod *= num_ways
    print(prod)