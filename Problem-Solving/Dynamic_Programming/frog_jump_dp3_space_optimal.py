energy = [30, 10, 60, 10, 60, 50]
n = len(energy)
prev1 = 0
prev2 = 0
for index in range(1, n):
    jump2 = float('inf')
    jump1 = prev1 + abs(energy[index] - energy[index-1])
    if index > 1:
        jump2 = prev2 + abs(energy[index]-energy[index-2])
    curr_index = min(jump1, jump2)
    prev2 = prev1
    prev1 = curr_index    
print(curr_index)