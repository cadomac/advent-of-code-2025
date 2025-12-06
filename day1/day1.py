import math

inputData = [i.strip() for i in open('./input.txt', 'r')]
testData = [i.strip() for i in open('./test-input.txt', 'r')]

def part1():

    current_pos = 50
    count = 0

    def rotate(distance, direction):
        subtotal = int(current_pos + distance)
        if direction == 'L':
            subtotal = int(current_pos - distance)
        return subtotal % 100

    for input in inputData:
        direction = input[0]
        distance = int(input[1:])
        current_pos = rotate(distance, direction)
        if current_pos == 0:
            count += 1

    print(f"\nPart 1 | Password: {count}\n")

def part2():
    current_pos = 50
    count = 0

    def rotate(distance, direction):
        times_passed_zero = 0
        passes, rotation = divmod(distance, 100)
        times_passed_zero += passes

        if current_pos + rotation >= 100 and direction == 'R':
            times_passed_zero += 1
        if current_pos and current_pos - rotation <= 0 and direction == 'L':
            times_passed_zero += 1
        new_pos = int(current_pos + rotation) if direction == 'R' else int(current_pos - rotation)
        new_pos %= 100
        
        return [new_pos, times_passed_zero]
            

    for input in inputData:
        direction = input[0]
        distance = int(input[1:])
        current_pos, times_passed_zero = rotate(distance, direction)
        count += times_passed_zero

    print(f"Part 2 | Password: {count}\n")

part1()
part2()