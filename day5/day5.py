import re
from operator import itemgetter

testFile = open('test.txt', 'r').read()
inputFile = open('input.txt', 'r').read()

def split_on_empty_lines(s):
    # greedily match 2 or more new-lines
    blank_line_regex = r"(?:\r?\n){2,}"

    return re.split(blank_line_regex, s.strip())

testData = [i.split('\n') for i in split_on_empty_lines(testFile)]
testData[0] = [[int(i.split('-')[0]), int(i.split('-')[1])] for i in testData[0]]
testData[1] = [int(i) for i in testData[1]]
inputData = [i.split('\n') for i in split_on_empty_lines(inputFile)]
inputData[0] = [[int(i.split('-')[0]), int(i.split('-')[1])] for i in inputData[0]]
inputData[1] = [int(i) for i in inputData[1]]

print(f"Test data: {testData}")

def part1(data):
    ranges = sorted(data[0], key=itemgetter(0))
    ids = data[1]
    fresh_ids = 0

    for i in ids:
        for r in ranges:
            start, end = r[0], r[1]
            if start <= int(i) <= end:
                fresh_ids += 1
                break
    return fresh_ids

def part2(data):
    ranges = sorted(data[0], key=itemgetter(0))
    merged_ranges = []

    pointer = 0
    while pointer < len(ranges):
        current_range = ranges[pointer]
        next_pointer = pointer + 1

        while next_pointer < len(ranges) and current_range[1] >= ranges[next_pointer][0]:
            current_range[1] = max(current_range[1], ranges[next_pointer][1])
            next_pointer += 1

        merged_ranges.append(current_range)
        pointer = next_pointer

    total_fresh_ids = 0
    for r in merged_ranges:
        start, end = r[0], r[1]
        total_fresh_ids += (end - start + 1)

    return total_fresh_ids

def main():
  
    print("Testing with example data:")
    print()
    
    test_result1 = part1(testData)
    
    print(f"\nExpected Part 1: 3, Got: {test_result1}")

    print("\nSolving with input data:")
    print()

    result1 = part1(inputData)

    print(f"\nPart 1 Result: {result1}")

    print("Testing with example data:")
    print()
    
    test_result2 = part2(testData)
    
    print(f"\nExpected Part 2: 14, Got: {test_result2}")

    print("\nSolving with input data:")
    print()

    result2 = part2(inputData)

    print(f"\nPart 2 Result: {result2}")

if __name__ == "__main__":
    main()