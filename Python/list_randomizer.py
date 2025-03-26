import random

old_list = [1, 2, 3, 4, 5] # Replace this list with any other list you want
index = []
new_list = []

while True:
    rand_n = random.randint(0, len(old_list)-1)
    
    if rand_n in index:
        continue
        
    index.append(rand_n)

    new_list.append(nums[rand_n])
        
    if len(old_list) == len(new_list):
        break

print(new_list)