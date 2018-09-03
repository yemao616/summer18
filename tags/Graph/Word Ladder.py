# Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:

# You must change exactly one character in every transformation
# Each intermediate word must exist in the dictionary
# Example :

# Given:

# start = "hit"
# end = "cog"
# dict = ["hot","dot","dog","lot","log"]
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.

# Note that we account for the length of the transformation path instead of the number of transformation itself.

#  Note:
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.



from collections import deque
class Solution:
    # @param start : string
    # @param end : string
    # @param dictV : list of strings
    # @return an integer
    def ladderLength(self, start, end, dictV):
        def construct_dict(word_list):
            d = {}
            for word in word_list:
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i+1:]
                    d[s] = d.get(s, []) + [word]
            return d
            
        def bfs_words(begin, end, dict_words):
            queue, visited = deque([(begin, 1)]), set()
            while queue:
                word, steps = queue.popleft()
                if word not in visited:
                    visited.add(word)
                    if word == end:
                        return steps
                    for i in range(len(word)):
                        s = word[:i] + "_" + word[i+1:]
                        neigh_words = dict_words.get(s, [])
                        for neigh in neigh_words:
                            if neigh not in visited:
                                queue.append((neigh, steps + 1))
            return 0
        
        d = construct_dict(dictV)
        return bfs_words(start, end, d)