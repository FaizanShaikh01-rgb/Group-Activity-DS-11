#Task-1 
#Given a list of integers, return the largest difference between any two elements, where the
#larger element appears after the smaller one. If no such pair exists, return 0.

def max_difference(nums):
    if not nums:
        return 0

    min_val = nums[0]
    max_diff = 0

    for num in nums[1:]:
        if num > min_val:
            max_diff = max(max_diff, num - min_val)
        else:
            min_val = num

    return max_diff

print(max_difference([2, 3, 10, 6, 4, 8, 1]))

#Task-2 
## given a string, return the first non-repeating character. If there are no one repeating characters then return None. 


def non_repeating(s):
    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1
    
    for char in s:
        if count[char] == 1:
            return char
    
    
    return None

print(non_repeating("Bareera"))

#Task-3 
#Given two strings, write a function to check if one is a permutation of the other. Return True if
#they are permutations, False otherwise.


def are_permutations(str1, str2):
    
    if len(str1) != len(str2):
        return False
    
    
    return sorted(str1) == sorted(str2)


print(are_permutations("abc", "cab")) 
print(are_permutations("abc", "def"))

#Task-4
def abc(arr):
    # Convert the list to a set to remove duplicates
    unique_numbers = set(arr)

    # If there are fewer than 2 unique numbers, return None
    if len(unique_numbers) < 2:
        return None

    # Initialize the largest and second largest values
    first = second = float('-inf')

    # Iterate through the unique numbers
    for num in unique_numbers:
        if num > first:
            # If current number is greater than the largest so far,
            # update both first an
#Task-5
def abc(arr, target):
    seen = set()           # To store numbers we've seen
    pairs = set()          # To store unique pairs that sum to the target

    for num in arr:
        complement = target - num
        if complement in seen:
            # Create a sorted tuple so (2,4) and (4,2) are treated the same
            pair = tuple(sorted((num, complement)))
            pairs.add(pair)
        # Add the number to the set of seen elements
        seen.add(num)

    return len(pairs)

# Exam

#Task-6

def abc(arr):
    seen = set()       # To track already-seen elements
    result = []        # To store the final list without duplicates

    for num in arr:
        if num not in seen:
            seen.add(num)      # Mark the number as seen
            result.append(num) # Keep it in the result

    return result

# Example in pdf
input_list = [1, 2, 2, 3, 4, 5, 1]
print(abc(input_list))  # Output: [1, 2, 3, 4, 5]

#Task-7

def powerset(nums):
    result = [[]]  # Start with the empty subset

    for num in nums:
        # For each number, add it to all existing subsets to create new ones
        new_subsets = [subset + [num] for subset in result]
        result.extend(new_subsets)  # Add the new subsets to the result

    return result

# Example in pdf
input_list = [1, 2, 3]
print(powerset(input_list))
# Output: [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]

#Task-8
def longest_increasing(lst):
    dp = [1] * len(lst)
    for i in range(len(lst)):
        for j in range(i):
            if lst[i] > lst[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

print(longest_increasing([10, 9, 2, 5, 3, 7, 101, 18]))

#Task-9
def max_product(nums):
    nums.sort()
    return max(nums[0] * nums[1], nums[-1] * nums[-2])

print(max_product([1, 10, -5, 1, 100]))

#Task-10
def most_frequent_char(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    max_count = 0
    result = ''
    for char in sorted(freq):
        if freq[char] > max_count:
            max_count = freq[char]
            result = char
    return result

print(most_frequent_char("aansJNLbbbc"))

#Task-11
def print_primes_less_than(n):
    for num in range(2, n):
        for i in range(2, num-1):
            if num % i == 0:
                break
        else:
            print(num,' ')

print_primes_less_than(10)

#Task-12
def sum_args(*args):
    return sum(args)

print(sum_args(2, 3, 4))

#Task-13
def highest_score(students):
    return max(students, key=students.get)

print(highest_score({"Alice": 85, "Bob": 90, "Charlie": 92}))

#Task-14
def apply_func(lst, func):
    return [func(x) for x in lst]

print(apply_func([1, 2, 3, 4], lambda x: x * x))

#Task-15
def compute(*args, operation='sum'):
    if operation == 'multiply':
        result = 1
        for num in args:
            result *= num
        return result
    else:
        return sum(args)

print(compute(1, 2, 3, 4, operation='multiply'))
