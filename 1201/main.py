import re

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
nums = digits + words

def get_digit(substr):
    if substr[:1] in nums:
        return int(substr[:1])
    if substr[:3] in nums:
        return words.index(substr[:3]) + 1
    if substr[:4] in nums:
        return words.index(substr[:4]) + 1
    if substr[:5] in nums:
        return words.index(substr[:5]) + 1

if __name__ == "__main__":
    file = "input.txt"
    lines = open("input.txt", 'r').readlines()
    
    sum = 0
    for line in lines:
        first_digit = min(filter(lambda x: x != -1, [line.find(n) for n in nums]))
        last_digit = max(filter(lambda x: x != -1, [line.rfind(n) for n in nums]))
        first_digit = get_digit(line[first_digit:])
        last_digit = get_digit(line[last_digit:])
        num = first_digit * 10 + last_digit
        print(num)
        sum += num
    print(sum)