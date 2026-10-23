
# Store first-year students' percentages
n = int(input("Enter number of students: "))

marks = []
for i in range(n):
    percentage = float(input(f"Enter percentage of student {i+1}: "))
    marks.append(percentage)


# i. Selection Sort
def selection_sort(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# ii. Bubble Sort
def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# Display sorted arrays
print("\nOriginal percentages:", marks)

selection = selection_sort(marks)
print("Selection Sort:", selection)

bubble = bubble_sort(marks)
print("Bubble Sort:", bubble)

# Display top five scores
print("\nTop Five Scores (Highest to Lowest):")
print(sorted(marks, reverse=True)[:5])
