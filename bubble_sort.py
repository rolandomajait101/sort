steps = 1

def bubble_sort(list):
    for i in range(len(list) - 1, 0, -1):
        for e in range(i):
            if list[e] > list[e + 1]:
                temp = list[e]
                list[e] = list[e + 1]
                list[e + 1] = temp
                globals()["steps"] = steps + 1


arr = input("Enter comma-seperated numbers (no space): ")
list = arr.split(",")

for i in range(0, len(list)):
    list[i] = int(list[i])


bubble_sort(list)
print(list)
print("Steps: " + str(steps))
