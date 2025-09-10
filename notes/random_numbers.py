#BZ 1st Random Numbers Notes
import random
#random number between 1-20
hi = random.randint(1,20)
print(hi)


statdice = []
for i in range(1,3):
    statdice.append(random.randint(1,6))
# Make me stats
stats = []
for i in range(0,6):
    stat_dice = []
    for i in range(0,4):
        stat_dice.append(random.randint(1,6))
    stat_dice.remove(min(stat_dice))
    stat = 0
    for i in stat_dice:
        stat += i

    stats.append(stat)
# im too lazy to format right now
print(stats)