from collections import defaultdict
from functools import reduce

nums = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
non_symbols = nums.union({'.'})

def gen_nums_boundaries(line):
    n = len(line)
    num_started = False
    start = None
    for i, c in enumerate(line):
        if (not num_started) and (c in nums):
            num_started = True
            start = i
            continue
        if (num_started) and (c not in nums):
            num_started = False
            yield (start, i)
            start = None
            continue
    if num_started:
        yield (start, n)

def is_symbol(x):
    return x not in non_symbols

def has_symbol(line):
    return any(map(is_symbol, line))

gear_pos_to_near_nums = defaultdict(lambda: []) # dict from (r, c) to list of numbers

if __name__ == "__main__":
    lines = open('input.txt', 'r').readlines()
    lines = [line.strip() for line in lines]
    total = 0
    for i, line in enumerate(lines):
        for (s, e) in gen_nums_boundaries(line):
            # print(line[s:e])
            number = int(line[s:e])
            s_index = max(0, s - 1)
            e_index = min(len(line), e + 1)
            prev_line = lines[i - 1] if i > 0 else None
            if prev_line is not None:
                prev_line = prev_line[s_index:e_index]
            next_line = lines[i + 1] if i < len(lines) - 1 else None
            if next_line is not None:
                next_line = next_line[s_index:e_index]

            this_line = line[s_index:e_index]
            star = -1
            while (prev_line is not None) and ((star := prev_line.find('*', star + 1)) != -1):
                gear_pos_to_near_nums[(i - 1, s_index + star)].append(number)

            star = -1
            while (star := this_line.find('*', star + 1)) != -1:
                gear_pos_to_near_nums[(i, s_index + star)].append(number)
            
            star = -1
            while (next_line is not None) and ((star := next_line.find('*', star + 1)) != -1):
                gear_pos_to_near_nums[(i + 1, s_index + star)].append(number)
    # print(total)
    print(gear_pos_to_near_nums)
    for nums in gear_pos_to_near_nums.values():
        if len(nums) == 2:
            print(nums)
            total += reduce(lambda y, x: y * x, nums, 1)
            
    print(total)
