from util import Stack, Queue  # These may come in handy
​
# Given two words (begin_word and end_word),
# and a dictionary's word list, return the shortest transformation
# sequence from begin_word to end_word, such that:
​
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list.
# Note that begin_word is not a transformed word.
# Note:
​
# Return None if there is no such transformation sequence.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume begin_word and end_word are non-empty and are not the same.
# Sample:
# begin_word = "hit"
# end_word = "cog"
# return: ['hit', 'hot', 'cot', 'cog']
​
# begin_word = "sail"
# end_word = "boat"
# ['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']
​
# beginWord = "hungry"
# endWord = "happy"
# None
​
​
# 2: Build the Graph
​
# Load words from dictionary
f = open('words.txt', 'r')
words = f.read().lower().split("\n")
f.close()
​
def get_neighbors(word):
    '''
    Get all words that are one letter
    away from the given word
    '''
    # Get same length words first
    result = []
    pass
​
​
# Create a counter that breaks if it goes higher than one and while loop through comparing
​
# Go through each word and build an adjacency list with each word one letter away
​
​
# Create an equality function
def words_are_neighbors(w1, w2):
    '''
    return True if words are one letter apart
    False otherwise
    '''
    list_word = list(w1)
    # Go through each letter in the word
    for i in range(len(list_word)):
        # swap with each letter in the alphabet
        for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
            # Check if that equals given word
            temp_word = list_word.copy()
            temp_word[i] = letter
            if "".join(temp_word) == w2:
                return True
    return False
​
def words_are_neighbors(w1, w2):
    print(f"comparing {w1} - {w2}")
    if len(w1) != len(w2):
        return False
    for i in range(len(w1)):
        if w1[:i] == w2[:i] and w1[i+1:] == w2[i+1:]:
            return True
    return False
​
​
# def words_are_neighbors(word1, word2):
#     for i in range(len(word1)):
#         list_word1 = list(word1)
#         list_word2 = list(word2)
#         list_word1.pop(i)
#         list_word2.pop(i)
#         if list_word1 == list_word2:
#             return True
​
words_are_neighbors("abc", "abd")
​
neighbors = {}
​
# Go through each word
for word in words:
    neighbors[word] = set()
    # Go through each potential neighbor
    for potential_neighbor in words:
        # Add to neighbors if they match
        if words_are_neighbors(word, potential_neighbor):
            neighbors[word].add(potential_neighbor)
​
​
def get_neighbors(word):
    return neighbors[word]
​
​
# 3: Traverse the graph (BFS)
def word_ladder(self, begin_word, end_word):
    # Create a queue
    q = Queue()
    # Enqueue a path to starting word
    q.enqueue( [begin_word] )
    # Create a visited set
    visited = set()
    # While queue is not empty:
    while q.size() > 0:
        # Dequeue path
        path = q.dequeue()
        # Grab the last word from the path
        w = path[-1]
        # Check if it's our target word
        if w == end_word:
            # If so, return path
            return path
        # Check if it's been visited
        # If not, mark as visited
        if w not in visited:
            # Enqueue path to each neighboring word
            for neighbor in get_neighbors(w):
                path_copy = path.copy()
                path_copy.append(neighbor)
                q.enqueue(path_copy)
​
​
print(word_ladder("sail", "boat"))