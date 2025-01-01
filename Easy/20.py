def isValid(s):
    """
    :type s_list: str
    :rtype: bool
    """
    s_list = list(s)
    inputs = {
        "(": ")",
        "[": "]",
        "{": "}",

    }
    not_peren = [value for key, value in inputs.items()]

    is_true = False

    for item in s_list:
        if item in not_peren:
            continue

        elif inputs[item] in s_list:
            s_list.remove(inputs[item])
            is_true = True

        elif inputs[item] not in s_list:
            return False

    return is_true


s1 = "(]([]}})))))"
print(isValid(s1))


