import random


dice_pool = input("What is the dice pool for the roll?: ")
values = []

hits = 0
glitches = 0

print("Rolling...")

count = 0



while count < dice_pool:
    dice_value = random.randrange(6) + 1

    values.append(dice_value)

    count = count + 1

print("Finished rolling dice")


# Calculate hits and glitches
for v in values:
    if v >= 5:
        hits = hits + 1
    elif v == 1:
        glitches = glitches + 1


print("Your dice values are: ")
print(values)

print(str(hits) + " Hits // " + str(glitches) + " Glitches")

if glitches > dice_pool / 2:
    print("!!!CRITICAL GLITCH!!!")
