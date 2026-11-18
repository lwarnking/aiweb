list = []
list_2 = []

letter = "b" 

word = "regenbogen"

indices_list = []
temp_list = []
#indices_list = [i for i, char in enumerate(word) if char == letter] 

indices_list = [i for i, ch in enumerate(word) if ch == letter]
temp_list.extend(indices_list)
#indices_list.append(indices)

print(indices_list, temp_list)
        



