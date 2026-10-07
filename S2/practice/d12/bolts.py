# Variables
request = None
found = False
bolts = {
    "4014",
    "4017",
    "8676",
    "14399-4",
    "7047"
}


# Greet
print("## Bolt stock check program v1 ##", end="\n\n")


# User input
while request == None:
    request = input("Enter bolt ISO standard id (e.g: 4014): ")


# Check bolts database (set)
for bolt in bolts:
    if (bolt == request):
        found = True


# Output
if (found == True):
    print("\u2705 Item in stock")
else:
    print("\u274C Item not found")
    
    

