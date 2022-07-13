from LinkedList import *

def mergeK_county(lists):
    if len(lists)>0:
        res = lists[0]
        for x in range(1,len(lists)):
            res = merge2_county(res,lists[x])
        return res
    return

def merge2_county(l1,l2):
    dummy = LinkedListNode(-1)
    prev = dummy
    while l1 and l2:
        if l1.data <= l2.data:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next
        prev = prev.next
    
    if l1 is not None:
        prev.next = l1
    
    if l2 is not None:
        prev.next = l2
    
    return dummy.next
    

# Driver code
a = create_linked_list([11,41,51])
b = create_linked_list([21,23,42])
c = create_linked_list([25,56,66,72])

print("All movie ID's from best to worse are:")
display(mergeK_county([a, b, c]))           