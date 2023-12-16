import re
import numpy as np

test_input = "d3_test_input.txt"
challenge_input = "d3_challenge_input.txt"

with open(challenge_input, "r") as input_file:
    raw_engine_schem = input_file.readlines() 

engine_schem = [l.strip() for l in raw_engine_schem]

def get_numbers():
    rows_as_array = np.array([list(x) for x in engine_schem])
    total = 0

    for idx, schem_row in enumerate(engine_schem):
        nums = re.finditer(r"\d+", schem_row)
        for num in nums:
            found_part = get_surrounding_parts(idx, num, len(schem_row), rows_as_array)
            if found_part:
                total += int(num.group())
       
    return total

def get_surrounding_parts(current_row, num, line_len, rows_as_array):
    found_part = False
    coordinates = []

    for row in [current_row - 1, current_row, current_row + 1]:
        for column in range(num.start() - 1, num.end() + 1):
            coordinates.append((row, column))

    for pair in coordinates:
        if 0 < pair[0] < len(rows_as_array) and 0 < pair[1] < line_len:
            array_val = rows_as_array[pair[0]][pair[1]]
            is_symbol = re.search(r"[^\d\.]", array_val)
            if is_symbol:
                found_part = True
                break
        if found_part:
            break

    return found_part            

total = get_numbers()
print(f"The sum of all part numbers in the engine schematic is {total}.")
