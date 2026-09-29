class Solution:
    def decodeMessage(self, key, message):
        mapping = {}
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        for ch in key:
            if ch != ' ' and ch not in mapping:
                mapping[ch] = alphabet[len(mapping)]

        result = ""

        for ch in message:
            if ch == ' ':
                result += ' '
            else:
                result += mapping[ch]

        return result
