# For Loop
print("For Loop:")
for i in range(1, 6):
    print(i)

# While Loop
print("\nWhile Loop:")
j = 1
while j <= 5:
    print(j)
    j += 1


# No increments/Decrements are used
# Python doesn't have a do-while loop.
# It can be simulated like this:

print("\nSimulated Do-While Loop:")
k = 1
while True:
    print(k)
    k += 1
    if k > 5:
        break