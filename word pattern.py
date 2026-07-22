class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()

        # Lengths must match
        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for ch, word in zip(pattern, words):
            # Check existing mappings
            if ch in char_to_word and char_to_word[ch] != word:
                return False

            if word in word_to_char and word_to_char[word] != ch:
                return False

            # Create mappings
            char_to_word[ch] = word
            word_to_char[word] = ch

        return True
