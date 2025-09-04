#BZ 1st String Methods Notes

awesome = 'Pickles and Mayo'

print(awesome)
print(awesome.upper())
print(awesome.lower())

#STUPID PROOFING
name = input("What's your name? ")
if name.strip().endswith('!'):
    name = name.strip().title()[:name.strip().find('!')]
else:
    name = name.strip().title()
#F string
print(f"What a nice name, {name}! It's very pretty!")

pi = 3.141592653589793238462643383279502

print(f"we all know pi is {pi:.2f}")

sentence = "The quick brown fox jumps over the lazy dog"
word = input("what to find? ")
start = sentence.index(word)
length = len(word)
print(sentence[start:start+length])
print(sentence.replace(word, word.swapcase()))