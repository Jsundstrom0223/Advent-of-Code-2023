import re

challenge_input = "d2_challenge_input.txt"
test_input = "d2_test_input.txt"

with open(challenge_input, "r") as input_file:
    raw_game_data = input_file.readlines() 

game_data = [l.strip() for l in raw_game_data]


def find_possible_games(data):
    limit_dic = {"red": 12, "green": 13, "blue": 14} 
    total = 0

    for line in game_data:
        just_data = line.split(":")[1]
        game_num = int(line.split(":")[0].split(" ")[1])
        game_cubes = re.split(r"[,;]", just_data)
        under_limit = True

        for cube in game_cubes:
            num_and_color = cube.lstrip().split(" ")
            num = int(num_and_color[0])
            color = num_and_color[1]
            
            limit = limit_dic[color]
            if num>limit:
                under_limit = False
                break

        if under_limit:
            total+= game_num

    return total

total = find_possible_games(game_data)
print(f"The sum of the IDs of the possible games is {total}.")
