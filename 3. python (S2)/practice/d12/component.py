# Variables
requestComponent = None
components = ["Bonnet", "Door_card", "Headlight", "Exhaust_manifold"]
found = False

Bonnet = {
    "Name": "Sport-light bonnet",
    "Material": "Carbon-fibre",
    "Mass": "7kg",
    "Cost": "$2000",
    "Quantity": 4
}

Door_card = {
    "Name": "Simple door card",
    "Material": "ABS",
    "Mass": "2kg",
    "Cost": "$100",
    "Quantity": 9
}

Headlight = {
    "Name": "Pro-bright headlight",
    "Material": "PMMA",
    "Mass": "5kg",
    "Cost": "$1000",
    "Quantity": 14
}

Exhaust_manifold = {
    "Name": "Sport manifold",
    "Material": "Cast iron",
    "Mass": "6kg",
    "Cost": "$1000",
    "Quantity": 4
}


# Greet
print("## Component database test v1 ##", end="\n\n")

print("Available components:")
print(components, end="\n\n")


# User input
while requestComponent == None:
    requestComponent = input("Enter component: ")


# Check if component exists
for num in range(0, len(components)):
    if (components[num] == requestComponent):
        found = True


# Output
if (found == True):
        if requestComponent =="Bonnet":
            print(Bonnet)

        elif requestComponent =="Door_card":
            print(Door_card)
        
        elif requestComponent =="Headlight":
            print(Headlight)
        
        elif requestComponent =="Exhaust_manifold":
            print(Exhaust_manifold)
else:
    print("\u274C Item not found")
    
    

