def strStr(haystack, needle):
    if not haystack and not needle:
        return 0

    first_index = -1
    num = 0
    index = 0
    interval = len(needle)

    for i in range(3):
        if haystack[index:interval] == needle:
            first_index = haystack.find(needle)
            num += 1

        index += len(needle)
        interval += len(needle)

    if first_index == -1:
        if needle in haystack:
            first_index = haystack.find(needle)
        else:
            first_index = -1

    return first_index

hay = "bbbbababbbaabbba"
nee = "abb"
print(strStr(hay, nee))
