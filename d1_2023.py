import regex

challenge_input = "d1_input.txt"
test_input = "test_input.txt"
p2_test_input = "d1_test_input_p2.txt"

with open(challenge_input, "r") as input_file:
    cal_doc_raw = input_file.readlines() 

cal_doc = [l.strip("\n") for l in cal_doc_raw]

def get_cal_values(lines):
    cal_val_sum = 0
    for p1_line in lines:
        cal_value = join_digits(p1_line)
        cal_val_sum += cal_value

    return cal_val_sum
 
def join_digits(line):
    digits = [char for char in line if char.isdigit()]
    if len(digits) >= 2:
        cal_value = "".join([digits[0], digits[-1]])
    else: 
        digits.append(digits[0])
        cal_value = "".join(digits)
    
    return int(cal_value)

def p2_get_cal_vals(lines):
    spelled_out_dic = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", 
                       "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    p2_cal_val_sum = 0

    for p2_line in lines: 
        line_as_list = list(p2_line)
        pattern = r"(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)"
        spelled_out_nums = regex.finditer(pattern, p2_line, overlapped=True)
        
        for i in spelled_out_nums:
            as_numeral = spelled_out_dic.get(i.captures()[0])
            line_as_list[i.start()] = as_numeral
            
        p2_cal_val = join_digits(line_as_list) 
        p2_cal_val_sum += p2_cal_val
        
    return p2_cal_val_sum

cal_val_sum = get_cal_values(cal_doc)
p2_cal_val_sum = p2_get_cal_vals(cal_doc)
print(f'Calibration values for P1 and P2: {cal_val_sum} and {p2_cal_val_sum }.')
