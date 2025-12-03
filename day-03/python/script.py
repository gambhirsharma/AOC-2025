

# 987654321111111
# 811111111111119
# 234234234234278
# 818181911112111




# def compute(batch): 
#     digit = list(batch)
#
#             # index , value
#     max_tenth = [0, 0]
#     max_oneth = 0 #only value
#     for i in range(len(digit)):
#         current_digit = int(digit[i])
#         if current_digit > max_tenth[1]: 
#             if max_tenth[0] == i - 1: 
#                 max_oneth = max_tenth[1]
#                 for j in range()
#             max_tenth = [i, current_digit]
#
#
#     # print(f"max for {batch} is {max[1]}")
#     num = max_tenth[1]
#
#     return num

# def max_joltage(bank):
#     digits = [int(d) for d in bank]
#     best = -1
#
#     # choose first digit (i)
#     for i in range(len(digits) - 1):
#         # choose second digit (j)
#         for j in range(i + 1, len(digits)):
#             value = digits[i] * 10 + digits[j]
#             if value > best:
#                 best = value
#     return best

def max_joltage_k(bank, k):
    digits = [int(d) for d in bank]
    stack = []
    to_remove = len(digits) - k  # how many digits we are allowed to drop

    for d in digits:
        # Remove smaller digits from stack if we can still drop
        while to_remove > 0 and stack and stack[-1] < d:
            stack.pop()
            to_remove -= 1
        stack.append(d)

    # If we still haven't removed enough, cut from the end
    return int("".join(str(d) for d in stack[:k]))



def main(): 
    file_path = '../data/data.txt'
    # file_path = '../data/demo.txt'

    result = []
    with open (file_path, 'r') as file: 
        data = file.read().strip().split('\n')
        for x in range(len(data)): 
            # large_number = compute(data[x])
            # large_number = max_joltage(data[x])
            large_number = max_joltage_k(data[x], 12)
            # print(x, data[x])
            result.append(large_number)

    print(f" The sum of the largest joltage numbers is: {sum(result)}")

    return 0

if __name__ == "__main__":
    main()
