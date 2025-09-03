inputs = []
words = [
         "a first name", 
         "a type of animal (plural)", 
         "the same animal (singular)", 
         "an adjective",
         "a meal",
         "another adjective",
         "a type of building",
         "a noun",
         "another noun",
         "a past tense verb",
         "any number",
         "another past tense verb"
         ]
def prompt(prompt):
    return input("Input " + prompt + " > ")

for i in words:
    inputs.append(prompt(i).lower())

print(inputs[0].capitalize() + " and the three " + inputs[1])
print("Once upon a time there was a " + inputs[3] + " family of three " + inputs[1] + ". They loved to eat " + inputs[4] + ". One day, while waiting for their " + inputs[4] + " to cool, they decided to take a walk. Little did they know, while they were out taking a walk, " + inputs[5] + " " + inputs[0] + " strolled into their " + inputs[6] + ". Upon seeing the yummy " + inputs[4] + " (which was " + inputs[0] + "'s favorite " + inputs[7] + "), they immediately grabbed a " + inputs[8] + " and " + inputs[9] + " it all up! After that, " + inputs[0] + " decided to take a nap. When the " + inputs[2] + " family got home, they saw their empty bowl of " + inputs[4] + " and " + inputs[0] + " asleep on their couch. Putting " + inputs[10] + " and " + inputs[10] + " together, they "+ inputs[11] + " " + inputs[0] + " far, far, away. " + inputs[5] + " " + inputs[0] + " was never seen again.")
