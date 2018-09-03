# An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:

# a) it                      --> it    (no abbreviation)

#      1
# b) d|o|g                   --> d1g

#               1    1  1
#      1---5----0----5--8
# c) i|nternationalizatio|n  --> i18n

#               1
#      1---5----0
# d) l|ocalizatio|n          --> l10n
# Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

# Example: 
# Given dictionary = [ "deer", "door", "cake", "card" ]

# isUnique("dear") -> false
# isUnique("cart") -> true
# isUnique("cane") -> false
# isUnique("make") -> true


class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        
        self.dictionary = {}
        
        for word in dictionary:
            if len(word) > 2:
                abbr = word[0] + str(len(word)-2) + word[-1]
            else:
                abbr = word
            
            if abbr not in self.dictionary:
                self.dictionary[abbr] = {word}
            else:
                self.dictionary[abbr].add(word)
        

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        if len(word) > 2:
            abbr = word[0] + str(len(word)-2) + word[-1]
        else:
            abbr = word
        
        return abbr not in self.dictionary or (word in self.dictionary[abbr] and len(self.dictionary[abbr]) == 1)
            

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)



class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.d = {}
        wordset = set()
        for word in dictionary:
            if word != '' and word not in wordset:
                k = (word[0], word[-1], len(word))
                if k in self.d:
                    self.d[k] = False
                else:
                    self.d[k] = word
            wordset.add(word)

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word == '':
            return True
        k = (word[0], word[-1], len(word))
        return k not in self.d or self.d[k] == word


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)