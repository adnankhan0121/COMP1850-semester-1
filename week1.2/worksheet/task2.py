# Worksheet 1.2: Task 2 Solution
import sys
import util

numbers = util.read_numbers()

if len(numbers) == 0:
    print("Error: no numbers provided", file=sys.stderr)
    sys.exit()

numbers.sort()
minimun = min(numbers)
maximun = max(numbers)
mean = sum(numbers) / len(numbers)
middle = len(numbers) // 2
if len(numbers) % 2 == 1:
   median = numbers[middle]
else:
    median = (numbers[middle - 1] + numbers[middle]) / 2
print(f"Minimum = {minimun}")
print(f"Maximum = {maximun}")
print(f"Mean = {mean}")
print(f"Median = {median}")