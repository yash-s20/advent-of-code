if __name__ == "__main__":
    lines = open('input.txt', 'r').readlines()
    s = 0
    for line in lines:
        numbers = [int(x) for x in line.split()]
        triangle_edge = [numbers[-1]]
        while not all(map(lambda x: x == 0, numbers)):
            new_numbers = numbers.copy()
            new_numbers = list(map(lambda x, y: x - y, new_numbers[1:], new_numbers[:-1]))
            triangle_edge.append(new_numbers[-1])
            numbers = new_numbers
        final_num = 0
        for num in reversed(triangle_edge):
            final_num += num
        print(final_num)
        s += final_num
    print(s)
