def compute(start_number, x): 
    num_store = start_number
    dir = x[0]
    num = int(x[1:])
    zero_pass = 0

    if dir == 'L':
        num_store = (start_number - num) % 100
        # Count how many times we pass through 0 going left
        if start_number == 0:
            zero_pass = num // 100
        elif num >= start_number:
            zero_pass = 1 + (num - start_number) // 100
        else:
            zero_pass = 0
    elif dir == 'R':
        num_store = (start_number + num) % 100
        # Count how many times we pass through 0 going right
        zero_pass = (start_number + num) // 100
    else: 
        raise ValueError("Invalid direction")

    return num_store, zero_pass

def main(): 
    file_path = '../data/data.txt'
    # file_path = '../data/demo.txt'
    output_arr = []
    num_store = 50 
    total_zero = 0 
    with open (file_path, 'r') as file: 
        data = file.read().strip().split('\n')

    for line in data:
        num_store, zero_pass = compute(num_store, line)
        total_zero += zero_pass
        print(f'Current number: {num_store}, Zero passed this move: {zero_pass}')
        output_arr.append(num_store)
        print(output_arr)

    # For Part 1: uncomment the line below to count final positions at 0
    # total_zero += output_arr.count(0)
    
    # For Part 2: zero_pass already includes all passes through 0
    print(f'The total zero passed is: {total_zero}')

    return 0

if __name__ == "__main__":
    main()
