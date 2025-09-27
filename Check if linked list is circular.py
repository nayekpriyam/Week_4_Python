def is_circular(head):
    if not head:
        return True
    curr = head.next
    while curr and curr != head:
        curr = curr.next
    return curr == head

print(is_circular(cll.head))  
