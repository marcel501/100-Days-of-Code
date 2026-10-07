# Constants
TOL_LOW = 55
TOL_HI = 60

# Input
measure = None
while measure is None:
    # Handle except errors due to non-integers
    try:
        measure = int(input("Input measure (mm): "))
    except ValueError:
        print("Invalid integer!")

# Output
if (measure >= TOL_LOW and measure <= TOL_HI):
    print("Accepted")
else:
    print("Rejected, acceptable range: 55<=X<=60")

