"""Best Practice: Don't modify the parameters in a function"""

def add_one_to_each(list_of_nums):
    nums = list_of_nums.copy()

    for index in range(len(nums)):
        nums[index] += 1

    return nums

some_list = [1, 2, 3, 4, 5]

modified_list = add_one_to_each(some_list)

print(modified_list)


"""A common alternative to copy()"""

# the following syntax creates a 'sublist' containing ALL the values
list_to_copy = ['person', 'car', 'airplane']
another_list = list_to_copy[:]

another_list.append('building')

print(list_to_copy)
print(another_list)