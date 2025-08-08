# In Python, the iterator protocol is what allows an object to be used in a for-loop (and other contexts that expect iterable data).
# There are two methods you need:
# 	1.	__iter__()
# 	•	Called once at the start of iteration—e.g. by iter(obj)
# 	•	Must return an iterator object. Often that’s self, if your class implements both methods.
# 	2.	__next__()
# 	•	Called repeatedly by the loop to get each successive item.
# 	•	When there are no more items, it must raise StopIteration to signal the end.

# - Generators simplify iterator creation: a function with yield
#   automatically provides __iter__() and __next__().
# - For reusable iterables, consider using a generator function


import random


class Playlist:
    def __init__(self, songs, shuffle=False):
        self.songs = songs
        self.index = 0

        if shuffle:
            random.shuffle(self.songs)

    def __iter__(self):
        return self

    # Define a magic method to iterate through songs
    def __next__(self):
        if self.index >= len(self.songs):
            raise StopIteration
        # Pull the next song, increment index, and return
        song = self.songs[self.index]
        self.index += 1

        return song


# Shuffle a Playlist, use for loop to iterate through
favorite_songs = Playlist(
    ["Ticking", "Tiny Dancer", "Blinding Lights", "One Dance"], shuffle=True
)

for song in favorite_songs:
    print(song)


##### Generator way (simpler)


class Playlist2:
    def __init__(self, songs):
        self.songs = songs

    def __iter__(self):
        for song in self.songs:
            yield song


favorite_songs2 = Playlist2(["Ticking", "Tiny Dancer", "Blinding Lights", "One Dance"])

for song in favorite_songs2:
    print(song)


#######


# Version 1: Using __iter__ and __next__
class Lottery:
    def __init__(self, count):
        self.count = count
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.count:
            raise StopIteration
        self.current += 1
        return random.randint(1, 100)


# Version 2: Using a generator
class Lottery2:
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        for _ in range(self.count):
            yield random.randint(1, 100)


# Both work the same way:
for num in Lottery(3):
    print(f"Lottery number: {num}")

for num in Lottery2(3):
    print(f"Lottery2 number: {num}")
