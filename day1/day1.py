import math

current_pos = 50
count = 0

def rotate(distance, direction):
    subtotal = int(current_pos + distance)
    if direction == 'L':
        subtotal = int(current_pos - distance)
    return subtotal % 100

with open('./input.txt', 'r') as file:
    while line := file.readline():
        line = line.strip()
        direction = line[0]
        distance = int(line[1:])
        print(f"Current position: {current_pos}, {line}")
        current_pos = rotate(distance, direction)
        print(f"New position: {current_pos}")
        if current_pos == 0:
            count += 1

print(f"Final position: {current_pos}, Password: {count}")