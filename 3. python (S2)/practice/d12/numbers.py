# Variables
numbers = []
mode = None
temp = None
smallest = None


# Greet
print("Algorithm selector program", end="\n\n")


# User input 
while (len(numbers) == 0):
    numbers = list(map(int, input("Enter numbers separated by a space: ").split()))

while (mode == None or mode > 2 or mode < 1):
    mode = int(input("Enter mode (1: Loop sort, 2: Loop search): "))


# Apply algorithm
match mode:
    case 1:
        # Selection sort (From smallest)
        
        # Round iteration
        for i in range(0, len(numbers) - 1):

            # Number iteration
            for j in range(i + 1, len(numbers)):
                if (numbers[i] > numbers[j]):
                    temp = numbers [i]
                    numbers[i] = numbers[j]
                    numbers[j] = temp

    case 2:
        # Linear search
        
        smallest = numbers[0]
        
        # Number iteration
        for num in range(1, len(numbers)):
            if smallest > numbers[num]:
                smallest = numbers[num]


# Output
if (mode == 1):
    print("Sorted list: ", numbers)
else:
    print("Smallest number: ", smallest)
