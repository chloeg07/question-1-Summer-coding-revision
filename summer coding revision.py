numbers = []
for i in range(5):
    num = float(input("Enter number {}: ".format(i+1)))
    numbers.append(num)
    
print("Orignal list:", numbers)

for i in range(len(numbers)):
    numbers[i] += 1
    
print("Updated list:", numbers)

all_increased = all(numbers[i] == (numbers[i-1]+ 1) for i in range(1, len(numbers)))
