def print_numbers(loop_count):
    if loop_count <= 0:
        print("Invalid loop count")
        return

    for i in range(5):
        print(i + 1)


loop_count = 5
print_numbers(loop_count)