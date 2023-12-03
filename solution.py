'''Advent of Code 2022 Day 1 Solution'''
import itertools

with open("example.txt","r",encoding='utf-8') as example:
    EXAMPLE_LIST = example.read()

split = EXAMPLE_LIST.splitlines()

DELIMITER = ''

spl = [list(y) for x, y in itertools.groupby(split, lambda z: z == DELIMITER) if not x]

sum_list = []
for value_list in spl:
    value_list = [int(i) for i in value_list]
    sum_list.append(sum(value_list))

sum_list.sort()
print(f'The Elf with the most calories is carrying {sum_list[-1]}')
