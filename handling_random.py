from random import random,randint

words = ["asd","dsa","ddd","sss"]
# array_length = len(words)
# selection_raw = random()
# division = 1/array_length

# selected_index = int(selection_raw/division)
selected_index = randint(0,len(words)-1)


print(f"We selected {words[selected_index]}")








