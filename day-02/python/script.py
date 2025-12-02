def compute(batch): 
    final_batch = []
    batch_start, batch_end = batch.strip().split('-')
    num_range = num_btwn(int(batch_start), int(batch_end))
    for num in num_range: 
        # 3      333
        rep_num, num = get_pattern(num)
        # final_batch.append((num))
        if(rep_num != 0):
            final_batch.append(int(num))
    
    return final_batch

def num_btwn(start, end):
    return list(range(start, end +1))

# solution for part 2 
def get_pattern(n):
    s = str(n)
    for size in range(1, len(s)//2 + 1):
        if len(s) % size == 0:
            pattern = s[:size]
            if pattern * (len(s)//size) == s:
                return pattern, int(s)
    return 0, 0

# solution for part 1 
# def get_pattern(n):
#     s = str(n)
#     length = len(s)
#
#     # Only lengths divisible by 2 can be made of 2 repeats
#     if length % 2 != 0:
#         return 0, 0
#
#     half = length // 2
#     pattern = s[:half]
#
#     # Check if the number is pattern repeated exactly twice
#     if pattern * 2 == s:
#         return pattern, int(s)
#
#     return 0, 0

def main(): 
    file_path = '../data/data.txt'
    # file_path = '../data/demo.txt'

    result = []
    total = 0
    with open (file_path, 'r') as file: 
        data = file.read().strip().split(',')
        for x in range(len(data)): 
            batch = data[x]
            # result.append(compute(batch))
            result.extend(compute(batch))
    
    total = sum(result)

    print("Final Result: ", result)
    print("total: ", total)

    return 0

if __name__ == "__main__":
    main()
