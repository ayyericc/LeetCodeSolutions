# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def mergeTwoLists(list1, list2):

    if list2 == []:
        return list1

    else:
        for num in list2:
            list1.append(num)
        list1.sort()
        return list1
    #
    #
    # combined_list = list1 + list2
    # combined_list.sort()
    # return combined_list

list1 = [1,2,4]
list2 = []
print(mergeTwoLists(list1,list2))