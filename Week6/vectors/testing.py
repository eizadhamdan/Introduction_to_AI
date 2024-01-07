from vectors import *

print(distance(words['book'], words["novel"]))
print(distance(words["book"], words["breakfast"]))
print(distance(words["lunch"], words["breakfast"]))

print(closest_words(words["book"])[: 10])
print(closest_word(words["king"] - words["man"] + words["woman"]))
