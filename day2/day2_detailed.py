def read_input(filename):
    """Read and parse the input file."""
    with open(filename, 'r') as f:
        return f.read().strip().split(',')

def is_repeated_pattern_twice(num_str):
    """Check if a number is made of a pattern repeated exactly twice."""
    length = len(num_str)
    if length % 2 != 0:
        return False
    
    mid = length // 2
    first_half = num_str[:mid]
    second_half = num_str[mid:]
    
    return first_half == second_half

def is_repeated_pattern_multiple_times(num_str):
    """Check if a number is made of a pattern repeated at least twice."""
    length = len(num_str)
    
    # Try all possible pattern lengths from 1 to length//2
    for pattern_length in range(1, length // 2 + 1):
        if length % pattern_length == 0:  # Length must be divisible by pattern length
            pattern = num_str[:pattern_length]
            # Check if the entire string is this pattern repeated
            if pattern * (length // pattern_length) == num_str:
                return True
    
    return False

def solve_part1_detailed(ranges):
    """Solve part 1 with detailed output."""
    total = 0
    
    print("Part 1 - Finding patterns repeated exactly twice:")
    print("=" * 50)
    
    for range_str in ranges:
        start_str, end_str = range_str.split('-')
        start = int(start_str)
        end = int(end_str)
        
        invalid_ids = []
        for num in range(start, end + 1):
            num_str = str(num)
            if is_repeated_pattern_twice(num_str):
                invalid_ids.append(num)
                total += num
        
        if invalid_ids:
            print(f"{range_str}: {invalid_ids}")
        else:
            print(f"{range_str}: no invalid IDs")
    
    print(f"\nTotal: {total}")
    return total

def solve_part2_detailed(ranges):
    """Solve part 2 with detailed output."""
    total = 0
    
    print("\nPart 2 - Finding patterns repeated at least twice:")
    print("=" * 50)
    
    for range_str in ranges:
        start_str, end_str = range_str.split('-')
        start = int(start_str)
        end = int(end_str)
        
        invalid_ids = []
        for num in range(start, end + 1):
            num_str = str(num)
            if is_repeated_pattern_multiple_times(num_str):
                invalid_ids.append(num)
                total += num
        
        if invalid_ids:
            print(f"{range_str}: {invalid_ids}")
        else:
            print(f"{range_str}: no invalid IDs")
    
    print(f"\nTotal: {total}")
    return total

def main():
    # Test with example data
    test_data = read_input('base.txt')
    
    print("Testing with example data:")
    print()
    
    test_result1 = solve_part1_detailed(test_data)
    test_result2 = solve_part2_detailed(test_data)
    
    print(f"\nExpected Part 1: 1227775554, Got: {test_result1}")
    print(f"Expected Part 2: 4174379265, Got: {test_result2}")

if __name__ == "__main__":
    main()