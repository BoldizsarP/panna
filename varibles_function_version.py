step_sister = "    This is a fully detailed long text    "

def our_strip(data_array):
    result = ""
    have_we_met_non_space_character =False
    for character in data_array:
        if character == " " and have_we_met_non_space_character == False:
            # if kod
            continue

        if character != " ":
            have_we_met_non_space_character = True

        result += character
    return result

reverse_mid_result = our_strip(step_sister)[::-1]
final_result =  our_strip(reverse_mid_result)[::-1]

quick_final = our_strip(our_strip(step_sister)[::-1])[::-1]

print(f"What is this?->{quick_final}<-")