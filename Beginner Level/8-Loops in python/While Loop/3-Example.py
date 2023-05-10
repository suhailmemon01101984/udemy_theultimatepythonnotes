# Example 3: Print elements of a list until "stop" is found




my_list = ["apple", "banana", "cherry", "stop", "orange"]

i = 0 #start from 0 which is apple

#Stop when the loop reach 'stop'
while my_list[i] != "stop":
    print(my_list[i])
    i += 1

