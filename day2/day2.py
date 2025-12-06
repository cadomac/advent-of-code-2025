testData = open('base.txt', 'r').read().strip().split(',')
inputData = open('input.txt', 'r').read().strip().split(',')

def part1():
    result = 0
    for input in inputData:
        print(f"Processing range: {input}")
        startStr, endStr = input.split('-')
        start = int(startStr)
        end = int(endStr)
        startLength = len(startStr)
        endLength = len(endStr)
        if startLength % 2 != 0 and endLength % 2 != 0:
            continue
        
        if startLength <= 1 and endLength <= 1:
            continue

        if startLength == 1:
            start = 10
            startStr = str(start)

        newStart = start

        while newStart <= end:
            newStartLength = len(str(newStart))
            if (newStartLength % 2) != 0:
                if (len(str(end)) % 2 != 0):
                    break
                else:
                    newStart += (10 ** (newStartLength)) - newStart
                    continue
            firstHalf = int(str(newStart)[0:newStartLength//2])
            secondHalf = int(str(newStart)[newStartLength//2:])
            if firstHalf == secondHalf:
                print(f"Found: {newStart}")
                result += newStart
                newStart += 10 - int(str(secondHalf)[-1])
            else:
                newStart += 1

    print(f"\nPart 1 | Result: {result}\n")

def part2():
    return