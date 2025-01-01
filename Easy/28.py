def strStr(haystack, needle):
    if not haystack and not needle:
        return 0

    first_index = None
    num = 0
    index = 0
    interval = len(needle)

    for i in range(3):
        if haystack[index:interval] == needle:
            first_index = haystack.find(needle[0])
            num += 1
        index += len(needle)
        interval += len(needle)
    return first_index

hay = "sadbutsad"
nee = "sad"
print(strStr(hay, nee))
