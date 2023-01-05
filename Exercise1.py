##Exercise 1
##Adapt the code above to generate a 1000 character long string with weights based on the previous two characters.
# Make HTTP requests for internet reqources.

# Load Libraries
import random
import urllib.request

# The URL of a text version of Alice in Wonderland.
book_url = 'https://www.gutenberg.org/files/11/11-0.txt'

# Get the book.
book = list(urllib.request.urlopen(book_url))

# Decode the lines and strip line endings.
book = [line.decode('utf-8-sig').strip() for line in book]

# Get a sample paragraph - I looked for this by hand.
paragraph = ' '.join(book[58:63])

alice = paragraph.lower()

# All letters and a space.
chars = 'abcdefghijklmnopqrstuvwxyz '

# And strip anything that is not a letter or space.
alice = ''.join([c for c in alice if c in chars])
# Print a random character, for example.
#print(random.choice(chars))

# Get the length of alice.
N = len(alice)

# Get the whole book in one big string.
sbook = ''.join(book[26:]).lower()

################################################################
## This contains a dictionary, where chars = c and each values is contained in another dictortionary d
### ie go through the list of char twice... aa,ab,ac,ad...ba,bb,bc
twoghts = {c: {d:  sbook.count(c + d )  for d in chars} for c in chars}

## Picking the letters th as the starting point
pairs = 'th'

# Do the following N = 1000 times.
for i in range(1, 1000):
    # Get the weights where the previous character is the last character in twos.
    wt = twoghts[pairs[-2]]
    # Turn wt into a list, ordered by chars.
    wt = [wt[c] for c in chars]
    # Randomly pick the next character using those weights.
    nextc = random.choices(chars, weights=wt, k=1)[0]
    # Append the character to twos.
    pairs = pairs + nextc
    print(pairs)
