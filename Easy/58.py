def lengthOfLastWord(self, s):
    if len(s) == 0:
        return 0

    word_list = s.split()
    length = len(word_list[-1])
    return length