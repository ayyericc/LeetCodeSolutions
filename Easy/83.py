def deleteDuplicates(head):
    if not head:
        return []

    temp_list = []
    for num in head:
        if num not in temp_list:
            temp_list.append(num)

    return temp_list

head = [1,2,2,2,3,4,5,5,5,6,7,8,8,8,8,9]
print(deleteDuplicates(head))