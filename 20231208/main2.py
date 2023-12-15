def end_with(word, letter):
    return word[-1] == letter

def all_end_with(words, letter):
    return all(map(lambda x: end_with(x, letter), words))

if __name__ == "__main__":
    lines = open('input.txt', 'r').readlines()
    path = lines[0].strip()
    all_nodes = []
    graph = {}
    for line in lines[2:]:
        line = line.strip()
        if not line:
            continue
        node, succs = line.split(' = ')
        left, right = succs.strip('()').split(', ')
        # print(node, left, right)
        graph[node] = {'L': left, 'R': right}
        all_nodes.append(node)
    nodes = filter(lambda x: end_with(x, 'A'), all_nodes)
    step = 0
    n = len(path)
    # print(path)
    print(list(filter(lambda x: end_with(x, 'Z'), all_nodes)))
    nodes = list(nodes)
    print(nodes)
    # while not all_end_with(nodes, 'Z'):
    #     new_nodes = []
    #     for node in nodes:
    #         node = graph[node][path[step % n]]
    #         new_nodes.append(node)
    #     step += 1
    #     nodes = new_nodes
    for node in nodes:
        step = 0
        print(node, end=" ")
        num_reached = 0
        while num_reached < 5:
            node = graph[node][path[step % n]]
            step += 1
            if end_with(node, 'Z'):
                print(node, step, end=" ")
                num_reached += 1
                step = 0
        print()
    print(step)