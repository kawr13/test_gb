numbers = [1, 6, 8, 98, 4, 6, 7]
max = numbers[0]
index = 0
size = 7
while index < size:
    if numbers[index] > max:
        max = numbers[index]       
    index = index + 1
print (max)
