def get_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

my_list = [10, 20, 30, 40, 50]
print(f"The average is: {get_average(my_list)}")
