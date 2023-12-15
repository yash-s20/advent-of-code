if __name__ == "__main__":
    lines = open('input.txt', 'r').readlines()
    path = lines[0].strip()
    graph = {}
    for line in lines[2:]:
        line = line.strip()
        if not line:
            continue
        node, succs = line.split(' = ')
        left, right = succs.strip('()').split(', ')
        print(node, left, right)
        graph[node] = {'L': left, 'R': right}
    node = 'AAA'
    step = 0
    n = len(path)
    print(path)
    while node != 'ZZZ':
        node = graph[node][path[step % n]]
        step += 1
    print(step)