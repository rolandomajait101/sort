from turtle import position


position = -1
attempts = 1

# WHILE LOOP
def linear_search(list, n):
    i = 0
    while i < len(list):
        if list[i] == n:
            globals()["position"] = i
            return True
        i = i + 1
        globals()["attempts"] = attempts + 1
    return False


values = input("Enter any numbers that are comma-separated (no spaces):\n")
n = int(input("Please enter the number you want to search for: \n"))
list = values.split(",")

for i in range(0, len(list)):
    list[i] = int(list[i])


if linear_search(list, n):
    print("Found! Index #:", position)
    print("Took", attempts, "attempts to find the number")
else:
    print("not found")
