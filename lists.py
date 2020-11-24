digits = list("76457235487")
numbers = list("123456789")

print(digits)
more_numbers = numbers.copy()

print(more_numbers)
print(numbers is more_numbers)
print(numbers == more_numbers)

computer_parts = ["mouse", "keyboard", "ups", "cpu", "mousepad", "moniter"]
print(computer_parts)

#changes the 0th index element of the list to the the string assigned.
computer_parts[0] = "joystick"
print(computer_parts)

#changes all the elements of the list after index 3 to the list assigned.
computer_parts[3:] = ["only the moniter"]
print(computer_parts)

min_valid = 100
max_valid = 200
data = [2, 4, 111, 123, 145, 134, 128, 211, 222]

stop = 0

for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

del data[:stop]

print(data)

start = 0

for index in range(len(data) -1, -1, -1):
    if data[index] <= max_valid:
        start = index + 1
        break

del data[start:]
print(data)
