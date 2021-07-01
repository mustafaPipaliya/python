# total_sum = 0
# n = 1

# while total_sum < 200:
#     previous_sum = total_sum    #140    n = 7
#     total_sum += n ** 2         #204    n = 8

#     if total_sum > 200:
#         total_sum = previous_sum
#         n -= 1
#         break

#     n += 1
    
# print(f"Total Summation : {total_sum} at n = {n}")

total_sum = 0
n = 1

while total_sum < 200:
    current_square = n**2
    if total_sum + current_square > 200:
        break
    
    total_sum += current_square
    n += 1


print(total_sum)


