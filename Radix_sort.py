
# Store 10th class students' percentages
n = int(input("Enter number of students: "))

marks = []
for i in range(n):
    percentage = float(input(f"Enter percentage of student {i+1}: "))
    marks.append(percentage)


# Radix Sort for floating-point numbers
def radix_sort(arr):
    if not arr:
        return []

    # Convert percentages to integers (2 decimal places)
    factor = 100
    nums = [int(round(x * factor)) for x in arr]

    maximum = max(nums)
    exp = 1

    while maximum // exp > 0:
        output = [0] * len(nums)
        count = [0] * 10

        for num in nums:
            digit = (num // exp) % 10
            count[digit] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(len(nums) - 1, -1, -1):
            digit = (nums[i] // exp) % 10
            output[count[digit] - 1] = nums[i]
            count[digit] -= 1

        nums = output
        exp *= 10

    # Convert back to percentages
    return [num / factor for num in nums]


# Sort percentages
sorted_marks = radix_sort(marks)

print("\nSorted percentages (Ascending):")
print(sorted_marks)

# Display top five scores
print("\nTop Five Scores (Highest to Lowest):")
print(sorted(sorted_marks, reverse=True)[:5])
