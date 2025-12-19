testData = open('test.txt', 'r').readlines()
inputData = open('input.txt', 'r').readlines()

def generateMatrixRow(line):
    line = line.strip()
    return list(line)

def generateMatrix(data):
    matrix = []
    for line in data:
        matrix.append(generateMatrixRow(line))
    return matrix

def getAdjacentCells(matrix, rowIdx, cellPos):
    behindPos = cellPos -1
    frontPos = cellPos + 1
    abovePos = rowIdx - 1
    belowPos = rowIdx + 1
    adjacentCells = [
        (matrix[rowIdx][behindPos] if behindPos >= 0 else None),
        (matrix[rowIdx][frontPos] if frontPos < len(matrix[rowIdx]) else None),
        (matrix[abovePos][behindPos] if abovePos >= 0 and behindPos >= 0 else None),
        (matrix[abovePos][cellPos] if abovePos >= 0 else None),
        (matrix[abovePos][frontPos] if abovePos >= 0 and frontPos < len(matrix[rowIdx]) else None),
        (matrix[belowPos][behindPos] if belowPos < len(matrix) and behindPos >= 0 else None),
        (matrix[belowPos][cellPos] if belowPos < len(matrix) else None),
        (matrix[belowPos][frontPos] if belowPos < len(matrix) and frontPos < len(matrix[belowPos]) else None),
    ]
    return adjacentCells

def part1(data):
    accessible_rolls = 0
    dataMatrix = generateMatrix(data)
    for rowIdx, row in enumerate(dataMatrix):
        for cellPos, cell in enumerate(row):
            if cell == '@':
                targetGrid = getAdjacentCells(dataMatrix, rowIdx, cellPos)

                if targetGrid.count('@') < 4:
                    accessible_rolls += 1
    return accessible_rolls

def part2(data):
    total_accessible_rolls = 0
    rollsStillAccessible = True
    dataMatrix = generateMatrix(data)
    deletionMatrix = [["." for _ in range(len(dataMatrix[0]))] for _ in range(len(dataMatrix))]
    while rollsStillAccessible:
        accessible_rolls = 0
        for rowIdx, row in enumerate(dataMatrix):
            for cellPos, cell in enumerate(row):
                if cell == '@':
                    if deletionMatrix[rowIdx][cellPos] == 'X':
                        continue
                    else:
                        deletionMatrix[rowIdx][cellPos] = '@'

                    targetGrid = getAdjacentCells(dataMatrix, rowIdx, cellPos)

                    if targetGrid.count('@') < 4:
                        accessible_rolls += 1
                        deletionMatrix[rowIdx][cellPos] = 'X'

        if accessible_rolls == 0:
            rollsStillAccessible = False
        dataMatrix = deletionMatrix
        total_accessible_rolls += accessible_rolls
    return total_accessible_rolls

def main():
  
    print("Testing with example data:")
    print()
    
    test_result1 = part1(testData)
    
    print(f"\nExpected Part 1: 13, Got: {test_result1}")

    print("\nSolving with input data:")
    print()

    result1 = part1(inputData)

    print(f"\nPart 1 Result: {result1}")

    print("Testing with example data:")
    print()
    
    test_result2 = part2(testData)
    
    print(f"\nExpected Part 2: 43, Got: {test_result2}")

    print("\nSolving with input data:")
    print()

    result2 = part2(inputData)

    print(f"\nPart 2 Result: {result2}")

if __name__ == "__main__":
    main()