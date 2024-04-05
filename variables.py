a = "we code in python"
b = "ew deco no pytohn"
c = "    This is a fully detailed long text    "
# print(a==b)
# print(c==c.strip())

# print("Nearly the same")
# print(c)
# print(c.strip())

# For valami in lista, avagy valami vegye fel egyszer a lista osszes elemet
# es fusson le a belso kod
# for character in a:
#     # belso kod
#     print(character)

# "".strip()
# object1 = {"marka": "opel", "model": "citra"}

# object2 = {"marka": "opel", "model": "citra"}
# print(f"Are these two objects the same {object1=}, {object2=}? {object2==object1}")
first_result = ""
result2 = ""
have_we_met_non_space_character = False

for character in c:
    if character == " " and have_we_met_non_space_character == False:
        # if kod
        continue

    if character != " ":
        have_we_met_non_space_character = True

    first_result += character

# print(f"I'm only interested in values from 6 until the 9th = {first_result[6:14]}")
# print(
#     f"I'm only interested in values from 6 until the 9th, but in reverse = {first_result[13:5:-1]}"
# )
have_we_met_non_space_character = False

for character in first_result[::-1]:
    if character == " " and have_we_met_non_space_character == False:
        # if kod
        continue

    if character != " ":
        have_we_met_non_space_character = True

    result2 += character

# print(f"This is a result after mirroring the text ->{result2}<-")

final_result = result2[::-1]

num = 5

# print(f"This is our final result ->{final_result}<-")
# print(f"This is much easier ->{c.strip()}<-")

# print(f"Original ->{c}<- =>->{result2}-<")

# print(f"Making everything lowercase {final_result.lower()}")
# print(f"Making everything \"uppercase {final_result.upper()}")

# print(f'This is not the same {"ASD"} {"asd"} => {"asd"=="ASD"}')

print(f""" 
      
      '"''' "" 
      
      """)