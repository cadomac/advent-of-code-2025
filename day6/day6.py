import re
from functools import reduce

testData = open('test.txt', 'r').readlines()
inputData = open('input.txt', 'r').readlines()

numRegex = r"-?\d+"
operatorRegex = r"[+\-*/]"

def handleOperator(op, a, b):
    match op:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            return a / b
    return 0
        
def getOperators(data):
    return re.findall(operatorRegex, data[-1].strip())

def part1(data):
    operators = getOperators(data)
    numberOfProblems = len(operators)

    resultMap = {}

    numArr = [[] for _ in range(numberOfProblems)]
    for idx, line in enumerate(data):
        if idx == len(data) -1:
            break
        numbers = [int(i) for i in re.findall(numRegex, line)]
        for j in range(len(numbers)):
            if idx == 0:
                resultMap[j] = numbers[j]
            else:
                resultMap[j] = handleOperator(operators[j], resultMap[j], numbers[j])
        
    finalResult = reduce(lambda x, y: x + y, resultMap.values())

    return finalResult

def part2(data):
    operators = getOperators(data)
    currentProblem = len(operators) - 1
    allWhiteSpace = True
    finalResult = 0.0
    currentProblemNums = []

    for col in range(len(data[0]) - 2, -1, -1):
        currentNumber = ""
        currentOperator = ""
        for idx, line in enumerate(data):
            if line[col] != " ":
                allWhiteSpace = False
            if idx == len(data) -1:
                if re.match(operatorRegex, line[col]):
                    currentOperator = line[col]
                continue
            currentNumber += line[col] if not re.match(r"\\n|\s", line[col]) else ""
        
        if currentOperator != "":
            currentProblem -= 1
            currentProblemNums.append(int(currentNumber))
            problemSolution = 0
            for idx, n in enumerate(currentProblemNums):
                if idx == 0:
                    problemSolution = n
                else:
                    problemSolution = handleOperator(currentOperator, problemSolution, n)
            finalResult += problemSolution
            currentProblemNums = []
            currentOperator = ""
            allWhiteSpace = True
        elif not allWhiteSpace and currentNumber != "":
            currentProblemNums.append(int(currentNumber))
            allWhiteSpace = True

    return int(finalResult)

def main():
  
    print("Testing with example data:")
    print()
    
    test_result1 = part1(testData)
    
    print(f"\nExpected Part 1: 4277556, Got: {test_result1}")

    print("\nSolving with input data:")
    print()

    result1 = part1(inputData)

    print(f"\nPart 1 Result: {result1}")

    print("Testing with example data:")
    print()
    
    test_result2 = part2(testData)
    
    print(f"\nExpected Part 2: 3263827, Got: {test_result2}")

    print("\nSolving with input data:")
    print()

    result2 = part2(inputData)

    print(f"\nPart 2 Result: {result2}")

if __name__ == "__main__":
    main()