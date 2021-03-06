# Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the given sentence can be fitted on the screen.

# Note:

# A word cannot be split into two lines.
# The order of words in the sentence must remain unchanged.
# Two consecutive words in a line must be separated by a single space.
# Total words in the sentence won't exceed 100.
# Length of each word is greater than 0 and won't exceed 10.
# 1 ≤ rows, cols ≤ 20,000.
# Example 1:

# Input:
# rows = 2, cols = 8, sentence = ["hello", "world"]

# Output: 
# 1

# Explanation:
# hello---
# world---

# The character '-' signifies an empty space on the screen.
# Example 2:

# Input:
# rows = 3, cols = 6, sentence = ["a", "bcd", "e"]

# Output: 
# 2

# Explanation:
# a-bcd- 
# e-a---
# bcd-e-

# The character '-' signifies an empty space on the screen.
# Example 3:

# Input:
# rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]

# Output: 
# 1

# Explanation:
# I-had
# apple
# pie-I
# had--

# The character '-' signifies an empty space on the screen.


class Solution(object):
    def wordsTyping(self, sentence, rows, cols):	# Time Limit Exceeded!
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        res = 0
        i, n = 0, len(sentence)
        for row in xrange(rows):
            left = cols
            while left >= len(sentence[i]):
                left -= len(sentence[i]) + 1
                if i < n-1:
                    i += 1
                elif i == n-1:
                    i = 0
                    res += 1
        return res
                

class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        words = [len(word) for word in sentence]
        nwords, slen = len(words), sum(words) + len(words) - 1
        fixed_count = (cols + 1) // (slen + 1) * len(words)
        start = cols + 1 - (cols + 1) % (slen + 1) if cols >= slen else 0
        
        counts = [fixed_count] * nwords	
        for i in range(nwords):
            c = 0
            j = start
            while j + words[(i+c) % nwords] <= cols:
                j += words[(i+c) % nwords] + 1
                c += 1
            counts[i] += c    # records the number of words can be fitted for each row starting from wrods[i] 
        
        words_count = 0
        for i in range(rows):
            words_count += counts[words_count % nwords]
        return words_count // nwords

