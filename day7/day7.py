testData = open('test.txt', 'r').readlines()
inputData = open('input.txt', 'r').readlines()

def getStartIndex(row):
    return row.find('S')

def part1(data):
    timesSplit = 0
    currentColumns = {getStartIndex(data[0])}
    for i in range(1, len(data)):
        currentRow = data[i]
        newColumns = set()
        columnsToRemove = set()
        for col in currentColumns:
            if currentRow[col] == '^':
                newColumns.add(col+1)
                newColumns.add(col-1)
                columnsToRemove.add(col)
                timesSplit += 1
        currentColumns.difference_update(columnsToRemove)
        currentColumns.update(newColumns)
    
    return timesSplit

def part2(data):
    memo = {}

    def updateMemo(key, computeFunc):
        if key in memo:
            return memo[key]
        else:
            value = computeFunc()
            memo[key] = value
            return value
    
    def computeTimelines(rowIndex, colIndex):
        if rowIndex >= len(data):
            return 1  # Reached the bottom, count as one valid timeline
        elif data[rowIndex][colIndex] == '.':
            return updateMemo((rowIndex + 1, colIndex), lambda: computeTimelines(rowIndex + 1, colIndex))
        else:
            # Split has happened
            left = updateMemo((rowIndex + 1, colIndex - 1), lambda: computeTimelines(rowIndex + 1, colIndex - 1))
            right = updateMemo((rowIndex + 1, colIndex + 1), lambda: computeTimelines(rowIndex + 1, colIndex + 1))
            return left + right

    def countTimelines(rowIndex, colIndex):
        key = (rowIndex, colIndex)
        return updateMemo(key, lambda: computeTimelines(rowIndex, colIndex))
    
    return countTimelines(0, getStartIndex(data[0]))

def main():
  
    # print("Testing with example data:")
    # print()
    
    # test_result1 = part1(testData)
    
    # print(f"\nExpected Part 1: 21, Got: {test_result1}")

    # print("\nSolving with input data:")
    # print()

    # result1 = part1(inputData)

    # print(f"\nPart 1 Result: {result1}")

    print("Testing with example data:")
    print()
    
    test_result2 = part2(testData)
    
    print(f"\nExpected Part 2: 40, Got: {test_result2}")

    print("\nSolving with input data:")
    print()

    result2 = part2(inputData)

    print(f"\nPart 2 Result: {result2}")

if __name__ == "__main__":
    main()