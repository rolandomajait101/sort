steps = 0


def selection_sort(list):
    for i in range(len(list)):
        minimum = i

        for j in range(i, len(list)):
            if list[j] < list[minimum]:
                minimum = j

        temp = list[i]
        list[i] = list[minimum]
        list[minimum] = temp
        globals()["steps"] = steps + 1


values = input("Enter any numbers that are comma-separated (no spaces):\n")
list = values.split(",")

for i in range(0, len(list)):
    list[i] = int(list[i])

selection_sort(list)

print("Steps taken: " + str(steps))
