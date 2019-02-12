# PROBLEM : Given head of singly linked list and an integer k.
#           Remove the kth node FROM END of the list.

# Using two pointers
# Time : O(n) | Space : O(1)
def removeKthNodeFromEnd(head, k):
    spaces = 1
    first = head
    second = head
    while spaces <= k:
        spaces += 1
        second = second.next
    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    # We stop at the last node,
    # so that first points to node before node to be removed
    while second.next is not None:
        second = second.next
        first = first.next
    first.next = first.next.next
    return
