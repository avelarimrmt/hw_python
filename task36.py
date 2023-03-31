

def print_operation_table(operation, num_rows = 7, num_columns = 7):
    for x in range(1, num_rows + 1):
        nums = []
        for y in range(1, num_columns + 1):
            num = operation(x, y)
            nums.append(num) 

        print(*[f"{x:>3}"  for x in nums])
        



eval(f'{input()}')