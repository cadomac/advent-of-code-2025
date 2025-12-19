testData = open('example.txt', 'r').readlines()
inputData = open('input.txt', 'r').readlines()

def part1():
    totalJoltage = 0
    for line in inputData:
        tensDigit = 0
        onesDigit = 0
        for char in line.strip():
            value = int(char)
            if value > tensDigit and line.index(char) < len(line.strip()) - 1:
                tensDigit = value
                onesDigit = 0
            elif value > onesDigit:
                onesDigit = value
        lineJoltage = int(f"{tensDigit}{onesDigit}")
        totalJoltage += lineJoltage

    print(f"\nPart 1 | Total Joltage: {totalJoltage}\n")

part1()

def part2():
    totalJoltage = 0
    for line in inputData:
        joltageStr = ""
        line = line.strip()
        p = 0
        remaining = 12

        for position in range(12):
            latest_start = len(line) - remaining

            max_digit = '0'
            best_p = p

            for i in range(p, latest_start + 1):
                if line[i] > max_digit:
                    max_digit = line[i]
                    best_p = i
            
            joltageStr += max_digit
            p = best_p + 1
            remaining -= 1
    
        print(f"Joltage String: {joltageStr}")
        totalJoltage += int(joltageStr)

    print(f"\nPart 2 | Total Joltage: {totalJoltage}\n")
        
part2()
