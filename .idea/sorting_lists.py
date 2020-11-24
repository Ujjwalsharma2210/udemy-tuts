even = []
odd = []

for i in range(0, int(input("Enter a limit"))):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("{}\n{}".format(even, odd))

even.extend(odd)
even.sort(reverse=True)
print(even)
